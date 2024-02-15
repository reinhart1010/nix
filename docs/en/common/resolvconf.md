---
layout: page
title: common/resolvconf (English)
description: "Manage nameserver information."
content_hash: f9a57e455564b3de96e621e030acb52c70cfd060
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# resolvconf

Manage nameserver information.
Acts as an intermediary between programs that supply nameserver information and applications that use this information.
This page documents Debian's implementation of `resolvconf`.
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
