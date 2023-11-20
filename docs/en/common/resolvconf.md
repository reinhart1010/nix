---
layout: page
title: common/resolvconf (English)
description: "Manage nameserver information."
content_hash: e6796df60a70af92dc3ea6daf1e8c3cbb48ca189
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# resolvconf

Manage nameserver information.
Acts as an intermediary between programs that supply nameserver information and applications that use this information.
This tldr documents Debian's implementation of resolvconf.
More information: <https://manned.org/resolvconf.8>.

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
