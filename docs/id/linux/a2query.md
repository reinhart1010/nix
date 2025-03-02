---
layout: page
title: linux/a2query (Indonesia)
description: "Dapatkan konfigurasi yang dipakai saat ini (secara runtime) dari piranti peladen Apache dalam sistem operasi berbasis Debian."
content_hash: 838bbee2aca9cfefeb2620492aeb3402b7664eeb
last_modified_at: 2025-03-02
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2query

Dapatkan konfigurasi yang dipakai saat ini (secara runtime) dari piranti peladen Apache dalam sistem operasi berbasis Debian.
Informasi lebih lanjut: <https://manned.org/a2query>.

- Tampilkan daftar modul Apache yang sedang aktif:

`sudo a2query -m`

- Cek apakah suatu modul Apache sedang aktif:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_modul</span>

- Tampilkan daftar host maya (virtual hosts) yang sedang aktif:

`sudo a2query -s`

- Tampilkan jenis modul Multi Processing Module yang sedang aktif:

`sudo a2query -M`

- Tampilkan versi piranti peladen Apache:

`sudo a2query -v`
