---
layout: page
title: common/poetry (English)
description: "Manage Python packages and dependencies."
content_hash: 466d2a1cd99f10921f07245eb2db3f3c19345ace
related_topics:
  - title: italiano version
    url: /it/common/poetry.html
    icon: bi bi-globe
---
# poetry

Manage Python packages and dependencies.
More information: <https://python-poetry.org/docs>.

- Create a new Poetry project in the directory with a specific name:

`poetry new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Install a dependency and its subdependencies:

`poetry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Install a development dependency and its subdependencies:

`poetry add --dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency</span>

- Interactively initialize the current directory as a new Poetry project:

`poetry init`

- Get the latest version of all dependencies and update `poetry.lock`:

`poetry update`

- Execute a command inside the project's virtual environment:

`poetry run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
