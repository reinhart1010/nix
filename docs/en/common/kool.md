---
layout: page
title: common/kool (English)
description: "Build software development environments."
content_hash: bc84022d92e8e11e5be57cb7e186a4aeaf0458e3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kool

Build software development environments.
More information: <https://kool.dev/docs/>.

- Create a project using a specific preset:

`kool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">preset</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Run a specific script defined in the `kool.yml` file in the current directory:

`kool run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>

- Start/stop services in the current directory:

`kool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>

- Display status of the services in the current directory:

`kool status`

- Update to the latest version:

`kool self-update`

- Print the completion script for the specified shell:

`kool completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>
