# pylama:ignore=D100,D101,D102,D103,D104,D106,D107
from pydantic import BaseConfig, Extra


class Config(BaseConfig):
    extra = Extra.forbid
