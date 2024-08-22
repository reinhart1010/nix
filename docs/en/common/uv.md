---
layout: page
title: common/uv (English)
description: "A fast Python package and project manager."
content_hash: c941275c2ea9369fb0cb6f0b3ba7e0f0f00e55ac
last_modified_at: 2024-08-22
tldri18n_status: 2
---
# uv

A fast Python package and project manager.
Some subcommands such as `uv tool` and `uv python` have their own usage documentation.
More information: <https://docs.astral.sh/uv/reference/cli>.

- Create a new Python project in the current directory:

`uv init`

- Create a new Python project in a directory with the given name:

`uv init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Add a new package to the project:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a package from the project:

`uv remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Run a script in the project's environment:

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>

- Run a command in the project's environment:

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Update a project's environment from `pyproject.toml`:

`uv sync`

- Create a lock file for the project's dependencies:

`uv lock`
