---
layout: page
title: linux/run0 (English)
description: "Elevate privileges interactively."
content_hash: b3264f2cfde86b1fa935568ab77e2b6d41f584af
last_modified_at: 2024-07-16
tldri18n_status: 2
---
# run0

Elevate privileges interactively.
Similar to `sudo`, but it's not a SUID binary, authentication takes place via polkit, and commands are invoked from a `systemd` service.
More information: <https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- Run a command as root:

`run0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run a command as another user and/or group:

`run0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username|uid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--group</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name|gid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
