---
layout: page
title: common/poetry (English)
description: "Manage Python packages and dependencies."
content_hash: 4e5ddc89979e30c4a88530a021324c680bab7f78
last_modified_at: 2024-02-27
related_topics:
  - title: Deutsch version
    url: /de/common/poetry.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/poetry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# poetry

Manage Python packages and dependencies.
See also: `asdf`.
More information: <https://python-poetry.org/docs/cli/>.

- Create a new Poetry project in the directory with a specific name:

`poetry new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Install and add a dependency and its sub-dependencies to the `pyproject.toml` file in the current directory:

`poetry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Install the project dependencies using the `pyproject.toml` file in the current directory:

`poetry install`

- Interactively initialize the current directory as a new Poetry project:

`poetry init`

- Get the latest version of all dependencies and update `poetry.lock`:

`poetry update`

- Execute a command inside the project's virtual environment:

`poetry run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Bump the version of the project in `pyproject.toml`:

`poetry version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch|minor|major|prepatch|preminor|premajor|prerelease</span>

- Spawn a shell within the project's virtual environment:

`poetry shell`
