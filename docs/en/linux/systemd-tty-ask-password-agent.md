---
layout: page
title: linux/systemd-tty-ask-password-agent (English)
description: "List or process pending systemd password requests."
content_hash: 55dd90b7c460d1e4cde0c65c7ead399e654a1ca3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-tty-ask-password-agent

List or process pending systemd password requests.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-tty-ask-password-agent.html>.

- List all currently pending system password requests:

`systemd-tty-ask-password-agent --list`

- Continuously process password requests:

`systemd-tty-ask-password-agent --watch`

- Process all currently pending system password requests by querying the user on the calling TTY:

`systemd-tty-ask-password-agent --query`

- Forward password requests to wall instead of querying the user on the calling TTY:

`systemd-tty-ask-password-agent --wall`
