---
layout: page
title: linux/flock (English)
description: "Manage locks from shell scripts."
content_hash: 7f7db889d6a50137eabc81ec1143e3a768d84846
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# flock

Manage locks from shell scripts.
It can be used to ensure that only one process of a command is running.
More information: <https://manned.org/flock>.

- Run a command with a file lock as soon as the lock is not required by others:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/lock.lock</span>` --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Run a command with a file lock, and exit if the lock doesn't exist:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/lock.lock</span>` --nonblock --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Run a command with a file lock, and exit with a specific error code if the lock doesn't exist:

`flock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/lock.lock</span>` --nonblock --conflict-exit-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error_code</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`
