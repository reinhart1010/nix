---
layout: page
title: common/uv (English)
description: "A fast Python package and project manager."
content_hash: 256bcee86c5d87d0c764bf7a42d5015019f98fc2
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/uv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/uv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uv

A fast Python package and project manager.
Some subcommands such as `tool` and `python` have their own usage documentation.
More information: <https://docs.astral.sh/uv/reference/cli>.

- Create a new Python project in the current directory:

`uv init`

- Create a new Python project at the specified path:

`uv init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Add a new dependency to the project:

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove a dependency from the project:

`uv remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Run a script in the project's environment:

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>

- Run a command in the project's environment:

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Update a project's environment from `pyproject.toml`:

`uv sync`

- Create a lock file for the project's dependencies:

`uv lock`
