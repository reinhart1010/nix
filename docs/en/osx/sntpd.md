---
layout: page
title: osx/sntpd (English)
description: "An SNTP server."
content_hash: 0d8a239244fd9f01bd0b7ad667fef325429a184e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sntpd

An SNTP server.
It should not be invoked manually.
More information: <https://linux.die.net/man/8/snmpd>.

- Start the daemon:

`sntpd`

- Overwrite existing state with the local clock (stratum 1), for running a master/primary server, without synchronizing with another (higher stratum) server:

`sntpd -L`

- Use a custom file for the SNTP state:

`sntpd -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/state.bin</span>
