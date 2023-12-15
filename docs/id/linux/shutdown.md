---
layout: page
title: linux/shutdown (Indonesia)
description: "Matikan dan nyalakan ulang sistem komputer."
content_hash: 32d0987f585c0187fdd05115438893ecc188835a
last_modified_at: 2023-12-15
related_topics:
  - title: català version
    url: /ca/linux/shutdown.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/shutdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/shutdown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shutdown

Matikan dan nyalakan ulang sistem komputer.
Informasi lebih lanjut: <https://manned.org/shutdown.8>.

- Matikan ([h]alt) sistem secara segera:

`shutdown -h now`

- Nyalakan ulang ([r]eboot) segera:

`shutdown -r now`

- Nyalakan ulang dalam 5 menit:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Matikan sistem pada pukul 1 siang (menggunakan format 24 jam):

`shutdown -h 13:00`

- Batalkan proses mati atau penyalaan ulang yang telah dijadwalkan:

`shutdown -c`
