---
layout: page
title: linux/mkfs.ext4 (Indonesia)
description: "Membuat sistem file ext4 didalam sebuah partisi."
content_hash: b0d39692ceb8cb87fb378ebe87509ae0689274ae
related_topics:
  - title: English version
    url: /en/linux/mkfs.ext4.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkfs.ext4

Membuat sistem file ext4 didalam sebuah partisi.
Informasi lebih lanjut: <https://manned.org/mkfs.ext4>.

- Membuat sistem file ext4 di dalam partisi 1 di perangkat B (`sdb1`):

`sudo mkfs.ext4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- Membuat sistem file ext4 dengan label volume:

`sudo mkfs.ext4 -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_volume</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
