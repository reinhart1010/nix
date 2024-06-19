---
layout: page
title: osx/sntpd (English)
description: "An SNTP server."
content_hash: 2f793cbfad34a310aacab3270825608fc48b79d8
last_modified_at: 2024-06-19
tldri18n_status: 2
---
# sntpd

An SNTP server.
It should not be invoked manually.
More information: <https://keith.github.io/xcode-man-pages/sntpd.8.html>.

- Start the daemon:

`sntpd`

- Overwrite existing state with the local clock (stratum 1), for running a master/primary server, without synchronizing with another (higher stratum) server:

`sntpd -L`

- Use a custom file for the SNTP state:

`sntpd -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/state.bin</span>
