---
layout: page
title: windows/comp (Indonesia)
description: "Bandingkan isi antar kedua berkas atau himpunan berkas."
content_hash: d65dbd4e5e5b17cdb79cab162396f1381392c650
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/windows/comp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/comp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/comp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comp

Bandingkan isi antar kedua berkas atau himpunan berkas.
Gunakan wildcard (*) untukk membandingkan himpunan berkas.
Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- Bandingkan isi berkas secara interaktif:

`comp`

- Bandingkan isi antara kedua berkas:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas2</span>

- Bandingkan isi antara kedua himpunan berkas:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\direktori1</span>`\* `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\direktori2</span>`\*`

- Tampilkan perbedaan dalam format [d]esimal:

`comp /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas2</span>

- Tampilkan perbedaan dalam format [a]SCII:

`comp /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas2</span>

- Tampilkan nomor baris di mana perbedaan antar isi terdeteksi:

`comp /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas2</span>

- Bandingkan berkas-berkas tanpa menghiraukan penggunaan huruf besar/kecil ([c]ase-insensitive):

`comp /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas2</span>

- Hanya bandingkan isi 5 baris pertama antara kedua berkas:

`comp /n=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan\menuju\berkas2</span>
