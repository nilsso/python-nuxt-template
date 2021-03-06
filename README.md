# Python Prisma/Nuxt Proof of Concept

(TODO)

**Hard requirements:**
[Python 3.7 minimum (I think!)][python],
[Node][node]

**Soft requirements (for [Getting Started](#getting-started)):**
[Poetry][poetry],
[yarn][yarn]

[python]: #
[node]: #
[poetry]: #
[yarn]: #

### TODO

- [ ] Describe backend/frontend structure, choice of Prisma and Zod
- [ ] Link dependencies
- [ ] Dockerize
- [ ] Watcher to refresh backend/frontend schemas on modifying `./prisma/schema.prisma`
  (maybe also make backend/frontend schemas read only?)

## Getting Started

Patch the Prisma schema for both the backend and the frontend (Python required)
```bash
./update_schemas.py
```

In one shell:
- Setup the backend `venv`
- Generate the SQLite database and Prisma client
- Run the backend
```bash
(cd backend && poetry install && poetry run prisma db push && poetry run uvicorn backend.app:app --reload)
```

Then in another shell:
- Install Node dependencies
- Generate the Zod models via the Prisma schema
- Run the frontend
```bash
(cd frontend && yarn install && npx prisma generate && yarn dev)
```

And that's it! You can now navigate to [localhost:8000][backend] to view the full Python Starlite REST API.

[![Viewing the Starlite REST API](./doc/img/web-schema.png)][backend]

And navigate to [localhost:3000][frontend] for the frontend.

[![Viewing the frontend](./doc/img/frontend.png)][frontend]

[backend]: http://localhost:8000
[frontend]: http://localhost:3000
