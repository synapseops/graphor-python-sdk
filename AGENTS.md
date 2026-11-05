# Graphor Python SDK: agent contract

The official Python client for the Graphor public API, published to PyPI as `graphor`. This file is the contract for any agent or engineer working here. The release procedure is in [RELEASING.md](RELEASING.md).

## This repository is public

Everything here is visible to anyone, including commits, branch names, pull requests and their history. A push cannot be taken back.

- Write only about the public API and the behavior of this SDK.
- Refer only to what a reader of this repository can open. Never mention internal systems, hostnames, infrastructure, costs or customers.
- A pull request or a commit says what changes for someone using the SDK. It does not explain internal reasons or link to anything private.
- Never commit secrets, tokens or `.env` files.

## This code is maintained by hand

The code was once generated and no longer is, so every change is made by hand. The header `File generated from our OpenAPI spec` on many files is historical: those files can be edited like any other.

## Layout

- `src/graphor/resources/sources.py`: the API methods, sync and async.
- `src/graphor/types/`: request parameter and response types.
- `src/graphor/_client.py`, `_base_client.py`: the client, retries and transport.
- `api.md`: the list of public methods and types.
- `tests/api_resources/`: one test per method. `tests/`: client and utility tests.
- `examples/`: usage examples.

## Commands

| Task | Command |
|---|---|
| Install dependencies | `./scripts/bootstrap` |
| Lint and types | `./scripts/lint` |
| Tests | `./scripts/test` |
| Format | `./scripts/format` |
| Build | `uv build` |

The gates are lint, tests and build. CI runs them on every push. They need uv 0.9 or newer.

## Tests do not cover the endpoints

Every test in `tests/api_resources/` is skipped (`Mock server tests are disabled`), so a green run says nothing about whether a method works against the API. A new or changed method must be exercised by hand against the API before a release, and the pull request says how.

## Changing the API surface

The Python and TypeScript SDKs expose the same API, so a change here has a matching change in [graphor-typescript-sdk](https://github.com/synapseops/graphor-typescript-sdk).

- Same method and parameter names, adapted only to each language's conventions.
- A change here updates the method (sync and async), its types, `api.md`, its test and the README when it mentions it.
- Removing or renaming anything public is a breaking change: call it out in the changelog.

## Git

- Work on a branch and open a pull request. Never push to `main`; a maintainer merges.
- Commits use a conventional subject (`feat:`, `fix:`, `docs:`, `chore:`).
- Stage files by name. Before pushing, read the diff for anything the section on this repository being public forbids.
- Changes that are not user-visible do not need a release.
