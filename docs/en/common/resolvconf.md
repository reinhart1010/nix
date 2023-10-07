---
layout: page
title: common/resolvconf (English)
description: "Manage nameserver information."
content_hash: ea3bf9c330254d045ed794f338f8e46973f0b3d0
last_modified_at: 2023-10-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># resolvconf

Manage nameserver information.
Acts as an intermediary between programs that supply nameserver information and applications that use this information.
This tldr documents Debian's implementation of resolvconf.
More information: <https://manpages.ubuntu.com/manpages/resolvconf.8.html>.

- Add or override the IFACE.PROG record and run the update scripts if updating is enabled:

`resolvconf -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IFACE.PROG</span>

- Delete the IFACE.PROG record and run the update scripts if updating is enabled:

`resolvconf -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IFACR.PROG</span>

- Just run the update scripts if updating is enabled:

`resolvconf -u`

- Set the flag indicating whether `resolvconf` should run update scripts when invoked with `-a`, `-d` or `-u`:

`resolvconf --enable-updates`

- Clear the flag indicating whether to run updates:

`resolvconf --disable-updates`

- Check whether updates are enabled:

`resolvconf --updates-are-enabled`
