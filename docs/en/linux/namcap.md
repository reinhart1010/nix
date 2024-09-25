---
layout: page
title: linux/namcap (English)
description: "Check binary packages and source `PKGBUILD`s for common packaging mistakes."
content_hash: 18b3c9cc56e08ee71eb35fcd27ff4581183f14bd
last_modified_at: 2024-09-25
tldri18n_status: 2
---
# namcap

Check binary packages and source `PKGBUILD`s for common packaging mistakes.
More information: <https://manned.org/namcap.1>.

- Check a specific `PKGBUILD` file:

`namcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pkgbuild</span>

- Check a specific package file:

`namcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package.pkg.tar.zst</span>

- Check a file, printing extra [i]nformational messages:

`namcap -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
