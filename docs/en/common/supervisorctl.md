---
layout: page
title: common/supervisorctl (English)
description: "Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems."
content_hash: a81cf7931bcf91ff19055e0e7feddd9aad43194b
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# supervisorctl

Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems.
Supervisorctl is the command-line client piece of the supervisor which provides a shell-like interface.
More information: <http://supervisord.org>.

- Show the status of a process (or all processes if `process_name` is not specified):

`supervisorctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Start/stop/restart a process:

`supervisorctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- Start/stop/restart all processes in a group:

`supervisorctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>`:*`

- Show last 100 bytes of process `stderr`:

`supervisorctl tail -100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` stderr`

- Keep displaying `stdout` of a process:

`supervisorctl tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` stdout`

- Reload process config file to add/remove processes as necessary:

`supervisorctl update`
