---
layout: page
title: osx/sntp (English)
description: "A very Simple Network Time Protocol client program."
content_hash: 87c3b58ea6724d07a1edc097f59a55605bb3519f
last_modified_at: 2024-01-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/sntp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sntp

A very Simple Network Time Protocol client program.
More information: <https://keith.github.io/xcode-man-pages/sntp.1>.

- Query a specified SNTP server and display the time:

`sntp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>

- Synchronize the system clock with a specified SNTP server:

`sudo sntp -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>

- Enable debug logging:

`sntp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool.ntp.org</span>
