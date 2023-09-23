---
layout: page
title: common/devcontainer (English)
description: "Use a Docker container as a development environment."
content_hash: 7d68ed34df3850d6353284d302b127343d0dff4e
last_modified_at: 2023-09-23
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># devcontainer

Use a Docker container as a development environment.
More information: <https://containers.dev/>.

- Create and run a Dev Container:

`devcontainer up`

- Apply a Dev Container Template to a workspace:

`devcontainer templates apply --template-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_id</span>` --template-args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_args</span>` --workspace-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/workspace</span>

- Execute a command on a running Dev Container in the current workspace:

`devcontainer exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Build a Dev Container image from `devcontainer.json`:

`devcontainer build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/workspace</span>

- Open a Dev Container in VS Code (the path is optional):

`devcontainer open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/workspace</span>

- Read and print the configuration of a Dev Container from `devcontainer.json`:

`devcontainer read-configuration`
