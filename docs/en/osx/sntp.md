---
layout: page
title: osx/sntp (English)
description: "A very Simple Network Time Protocol client program."
content_hash: 87c3b58ea6724d07a1edc097f59a55605bb3519f
last_modified_at: 2024-01-04
tldri18n_status: 2
---
# sntp

A very Simple Network Time Protocol client program.
More information: <https://keith.github.io/xcode-man-pages/sntp.1>.

- Query a specified SNTP server and display the time:

`sntp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>

- Synchronize the system clock with a specified SNTP server:

`sudo sntp -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>

- Enable debug logging:

`sntp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>
