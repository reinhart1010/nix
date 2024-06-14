---
layout: page
title: common/ansiweather (Indonesia)
description: "Tampilkan kondisi cuaca saat ini ke dalam terminal."
content_hash: 004c70045cff979d44d012b2a42afbcde5a078d9
last_modified_at: 2024-06-14
related_topics:
  - title: Deutsch version
    url: /de/common/ansiweather.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ansiweather.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ansiweather

Tampilkan kondisi cuaca saat ini ke dalam terminal.
Informasi lebih lanjut: <https://github.com/fcambus/ansiweather>.

- Tampilkan ramalan cuaca ([f]orecast) selama tujuh hari ke depan bagi suatu [l]okasi, dengan satuan [u]nit ukur metrik:

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Tampilkan ramalan cuaca ([F]orecast) selama lima hari ke depan bagi lokasi saat ini, dengan tampilan [s]imbol serta informasi waktu matahari terbit dan terbenam ([d]aylight):

`ansiweather -F -s true -d true`

- Tampilkan informasi kecepatan angin ([w]ind) dan kelembapan udara ([h]umidity) bagi waktu dan lokasi saat ini:

`ansiweather -w true -h true`
