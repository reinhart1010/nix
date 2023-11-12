---
layout: page
title: linux/extrace (English)
description: "Trace exec() calls."
content_hash: 108be45a287e95f2b36b2a198e4a25519d99e5e1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# extrace

Trace exec() calls.
More information: <https://github.com/chneukirchen/extrace>.

- Trace all program executions occurring on the system:

`sudo extrace`

- Run a command and only trace descendants of this command:

`sudo extrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Print the current working directory of each process:

`sudo extrace -d`

- Resolve the full path of each executable:

`sudo extrace -l`

- Display the user running each process:

`sudo extrace -u`
