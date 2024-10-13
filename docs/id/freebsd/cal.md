---
layout: page
title: freebsd/cal (Indonesia)
description: "Tampilkan kalender dengan menyorot tanggal saat ini."
content_hash: de7b7e61e4dbe970a00b528a78d9da2f57bc294e
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/freebsd/cal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Tampilkan kalender dengan menyorot tanggal saat ini.
Informasi lebih lanjut: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Tampilkan kalender untuk bulan saat ini:

`cal`

- Tampilkan kalender untuk suatu tahun:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tahun</span>

- Tampilkan kalender untuk suatu bulan dalam tahun:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bulan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tahun</span>

- Tampilkan seluruh kalender untuk tahun ini:

`cal -y`

- Jangan sorot ([h]ighlight) tanggal hari ini dan tampilkan kalender untuk [3] bulan yang mencakup tanggal tersebut:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bulan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tahun</span>

- Tampilkan 2 bulan se[B]elum dan 3 setel[A]h bulan tertentu pada tahun berjalan:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bulan</span>

- Tampilkan hari [j]ulian (hari sejak awal tahun, dimulai dengan nilai satu untuk 1 Januari):

`cal -j`
