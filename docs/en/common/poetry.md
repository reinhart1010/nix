---
layout: page
title: common/poetry (English)
description: "Manage Python packages and dependencies."
content_hash: fd32c92a76c0d7c5940391b07d5c2c507da77f07
last_modified_at: 2024-01-09
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

- Install a dependency and its subdependencies:

`poetry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Install a development dependency and its subdependencies:

`poetry add --group dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Interactively initialize the current directory as a new Poetry project:

`poetry init`

- Get the latest version of all dependencies and update `poetry.lock`:

`poetry update`

- Execute a command inside the project's virtual environment:

`poetry run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Bump the minor version of the project in `pyproject.toml`:

`poetry version minor`
