#!/usr/bin/env python
# pylama:ignore=D100,D101,D102,D103,D104,D107
import argparse
import re
from itertools import chain
from pathlib import Path
from sys import stdout
from typing import Callable, Iterable, Iterator

mod_dir = Path(__file__).parent


SCHEMA_PATH = mod_dir / "prisma/schema.prisma"
BACKEND_GENERATOR_PATH = mod_dir / "prisma/backend.prisma"
FRONTEND_GENERATOR_PATH = mod_dir / "prisma/frontend.prisma"
BACKEND_SCHEMA_PATH = mod_dir / "backend/schema.prisma"
FRONTEND_SCHEMA_PATH = mod_dir / "frontend/prisma/schema.prisma"

OPTIONAL = re.compile(r"^\s+\w+\s+\w+\?")
RELATION = re.compile(r"^\s+\w+\s+\w+\s+@relation")
LIST = re.compile(r"^\s+\w+\s+\w+\[\]")
DATE = re.compile(r"^\s+\w+\s+Date(Time)?")
DECIMAL = re.compile(r"^\s+\w+\s+Decimal\s+@db.Decimal\((\d+),\s*(\d+)\)")


def anotate_node(f: Iterable[str]):
    for line in map(str.rstrip, f):
        endings = []
        if not line.startswith(r"//"):
            if is_nullable(line):
                endings.append("nullable()")
            if DATE.search(line):
                endings.append("custom(imports.isoDateString)")
            if (m := DECIMAL.search(line)) is not None:
                # p = m.group(1)  # precision
                # s = m.group(2)  # scale
                # endings.append(f'custom(imports.decimal({p},{s}))')
                endings.append("custom(imports.decimal)")
        if len(endings) > 0:
            yield line + f' /// @zod.{".".join(endings)}'
        else:
            yield line


def is_nullable(line: str) -> bool:
    if OPTIONAL.search(line):
        return True
    if LIST.search(line):
        return True
    if RELATION.search(line):
        return True
    return False


def process(
    schema_path: Path,
    generator_path: Path,
    processor: Callable[[Iterable[str]], Iterator[str]] | None = None,
):
    with open(schema_path) as _schema:
        with open(generator_path) as _generator:
            schema = map(str.rstrip, _schema)
            generator = map(str.rstrip, _generator)
            processed = processor(schema) if processor else schema
            for line in chain(processed, generator):
                yield line


def repad(lines: Iterable[str]) -> Iterator[str]:
    def _pad(line: str) -> str:
        return line + "\n"

    for line in map(_pad, lines):
        yield line


def process_to_file(
    out_path: Path,
    schema_path: Path,
    generator_path: Path,
    processor: Callable[[Iterable[str]], Iterator[str]] | None = None,
):
    with open(out_path, "w") as f:
        f.writelines(repad(process(schema_path, generator_path, processor)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--stdout", action="store_true")

    args = parser.parse_args()

    backend_lines = repad(process(SCHEMA_PATH, BACKEND_GENERATOR_PATH))
    frontend_lines = repad(process(SCHEMA_PATH, FRONTEND_GENERATOR_PATH, anotate_node))

    if args.stdout:
        stdout.writelines(backend_lines)
        stdout.writelines(frontend_lines)
    else:
        print(BACKEND_SCHEMA_PATH)
        with open(BACKEND_SCHEMA_PATH, "w") as f:
            f.writelines(backend_lines)
        with open(FRONTEND_SCHEMA_PATH, "w") as f:
            f.writelines(frontend_lines)
