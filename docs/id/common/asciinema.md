---
layout: page
title: common/asciinema (Indonesia)
description: "Rekam dan putar ulang sesi terminal, dan secara opsional membagikannya di <https://asciinema.org>."
content_hash: ffabb96d5e84cab5555dff5e659055ce118e0d08
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciinema.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asciinema.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciinema

Rekam dan putar ulang sesi terminal, dan secara opsional membagikannya di <https://asciinema.org>.
Lihat juga: `terminalizer`.
Informasi lebih lanjut: <https://docs.asciinema.org/manual/cli/usage>.

- Masuk dengan suatu akun asciinema.org:

`asciinema auth`

- Buat rekaman baru (hentikan dengan `Ctrl+D` atau ketik `exit`, kemudian pilih lokasi penyimpanan baik dengan mengunggah atau menyimpannya secara lokal):

`asciinema rec`

- Buat rekaman baru kemudian simpan ke dalam suatu berkas lokal:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/rekaman.cast</span>

- Putar ulang rekaman sesi terminal dari suatu berkas lokal:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/rekaman.cast</span>

- Putar ulang suatu rekaman sesi terminal yang dipublikasikan di <https://asciinema.org>:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_rekaman</span>

- Buat rekaman baru, dengan membatasi waktu diam/[i]dle terlama selama 2.5 detik:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--idle-time-limit</span>` 2.5`

- Tampilkan seluruh luaran/output terminal yang dikeluarkan selama sesi perekaman:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/rekaman.cast</span>

- Unggah suatu berkas hasil rekaman lokal menuju asciinema.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/rekaman.cast</span>
