---
layout: page
title: linux/runuser (English)
description: "Run commands as a user and group without asking for password (needs root privileges)."
content_hash: 80a518275d0845c2826b7011e5834b01fa65927c
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# runuser

Run commands as a user and group without asking for password (needs root privileges).
More information: <https://manned.org/runuser>.

- Run command as a different user:

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`'`

- Run command as a different user and group:

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>` -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`'`

- Start a login shell as a specific user:

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -l`

- Specify a shell for running instead of the default shell (also works for login):

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/sh</span>

- Preserve the entire environment of root (only if `--login` is not specified):

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --preserve-environment -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`'`
