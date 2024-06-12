---
layout: page
title: linux/agetty (English)
description: "Alternative `getty`: Open a `tty` port, prompt for a login name, and invoke the `/bin/login` command."
content_hash: fa92bf269efc82a80ae03f5f5adf3dc85d042cc6
last_modified_at: 2024-06-12
related_topics:
  - title: español version
    url: /es/linux/agetty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# agetty

Alternative `getty`: Open a `tty` port, prompt for a login name, and invoke the `/bin/login` command.
It is normally invoked by `init`.
Note: the baud rate is the speed of data transfer between a terminal and a device over a serial connection.
More information: <https://manned.org/agetty>.

- Connect `stdin` to a port (relative to `/dev`) and optionally specify a baud rate (defaults to 9600):

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- Assume `stdin` is already connected to a `tty` and set a timeout for the login:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--timeout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout_in_seconds</span>` -`

- Assume the `tty` is [8]-bit, overriding the `TERM` environment variable set by `init`:

`agetty -8 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">term_var</span>

- Skip the login (no login) and invoke, as root, another login program instead of `/bin/login`:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--skip-login</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--login-program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">login_program</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty</span>

- Do not display the pre-login (issue) file (`/etc/issue` by default) before writing the login prompt:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--noissue</span>` -`

- Change the root directory and write a specific fake host into the `utmp` file:

`agetty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/root_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-H|--host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fake_host</span>` -`
