---
layout: page
title: common/cupsd (English)
description: "Server daemon for the CUPS print server."
content_hash: 7c5229036dac8ef159f3ae792d90ac17c21b927f
last_modified_at: 2024-01-30
related_topics:
  - title: Nederlands version
    url: /nl/common/cupsd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cupsd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsd

Server daemon for the CUPS print server.
More information: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- Start `cupsd` in the background, aka. as a daemon:

`cupsd`

- Start `cupsd` on the [f]oreground:

`cupsd -f`

- [l]aunch `cupsd` on-demand (commonly used by `launchd` or `systemd`):

`cupsd -l`

- Start `cupsd` using the specified [`c`]`upsd.conf` configuration file:

`cupsd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cupsd.conf</span>

- Start `cupsd` using the specified `cups-file`[`s`]`.conf` configuration file:

`cupsd -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cups-files.conf</span>

- [t]est the [`c`]`upsd.conf` configuration file for errors:

`cupsd -t -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cupsd.conf</span>

- [t]est the `cups-file`[`s`]`.conf` configuration file for errors:

`cupsd -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cups-files.conf</span>

- Display help:

`cupsd -h`
