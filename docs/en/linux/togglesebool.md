---
layout: page
title: linux/togglesebool (English)
description: "Flip the current (non-persistent) values of SELinux booleans."
content_hash: d0ba9f6e6798cbc809632a162a7f4ff34d3dba68
last_modified_at: 2024-05-27
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/togglesebool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># togglesebool

Flip the current (non-persistent) values of SELinux booleans.
Note: This tool has been deprecated and often removed in favor of `setsebool`.
More information: <https://manned.org/man/togglesebool>.

- Flip the current (non-persistent) values of the specified booleans:

`sudo togglesebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virt_use_samba virt_use_usb ...</span>
