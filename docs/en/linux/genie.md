---
layout: page
title: linux/genie (English)
description: "Set up and use a \"bottle\" namespace to run systemd under WSL (Windows Subsystem for Linux)."
content_hash: acac9b787af500cfd731a6e5f08c347881414990
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# genie

Set up and use a "bottle" namespace to run systemd under WSL (Windows Subsystem for Linux).
To run these from Windows rather than an already-running distribution, precede them with `wsl`.
More information: <https://github.com/arkane-systems/genie>.

- Initialize the bottle (run once, at start):

`genie -i`

- Run a login shell inside the bottle:

`genie -s`

- Run a specified command inside the bottle:

`genie -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
