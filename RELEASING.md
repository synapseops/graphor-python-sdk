# Releasing

A published version cannot be replaced or changed. If one is wrong, publish a new one with the fix. Publishing is a deliberate step taken by a maintainer.

## Choosing the version

The SDK is before 1.0, so: a new feature or a breaking change bumps the minor (`0.26.0` to `0.27.0`), and a fix or a documentation change bumps the patch (`0.26.0` to `0.26.1`).

## Steps

1. On a branch `release/vX.Y.Z`, update the version in all three places:
   - `pyproject.toml`
   - `src/graphor/_version.py`
   - `uv.lock`, by running `uv lock` after the two above
2. Add the section to `CHANGELOG.md`, written for someone using the SDK. Call out breaking changes.
3. Run `bin/check-release-version X.Y.Z` and the gates: `./scripts/lint`, `./scripts/test`, `uv build`. All of them need uv 0.9 or newer.
4. Open a pull request and merge it.
5. Create the release from `main`, with a tag matching the version:

   ```sh
   gh release create vX.Y.Z --target main --title "vX.Y.Z" --notes-file <notes>
   ```

   Create it with a person's credentials: a release made with the default `GITHUB_TOKEN` of a workflow does not start other workflows.

6. Follow the `Publish PyPI` workflow, which runs on the published release and uses PyPI trusted publishing. It first checks that the tag matches every version location, and fails before publishing if not.

## Verifying

```sh
uv run --isolated --no-project --refresh-package graphor --with "graphor==X.Y.Z" python -c "import graphor; print(graphor.__version__)"
```

It must print the new version.

## If something goes wrong

- **The version check failed:** the tag points at a commit with the wrong version. Nothing was published. Release a new patch version; do not move the tag.
- **The workflow failed before publishing, for another reason:** fix the cause and run it from the Actions tab (`workflow_dispatch`), picking the tag under "Use workflow from". It refuses to run from a branch.
- **Last resort, a token from the shell:** `git checkout vX.Y.Z && read -rs PYPI_TOKEN && export PYPI_TOKEN && bash bin/publish-pypi`.
- **A published version is broken:** publish a fixed version, then yank the broken one on PyPI.
