---
layout: page
title: osx/sntpd (English)
description: "An SNTP server."
content_hash: bb9b484f87bd81c2e3939e6eb3596c1414f3be1b
---
# sntpd

An SNTP server.
It should not be invoked manually.

- Start the daemon:

`sntpd`

- Overwrite existing state with the local clock (stratum 1), for running a master/primary server, without synchronizing with another (higher stratum) server:

`sntpd -L`

- Use a custom file for the SNTP state:

`sntpd -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/state.bin</span>
