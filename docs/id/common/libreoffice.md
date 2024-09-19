---
layout: page
title: common/libreoffice (Indonesia)
description: "Antarmuka baris perintah untuk LibreOffice, aplikasi perkantoran mahir dan gratis."
content_hash: ef1f1e33570981d1b7eade63db52b47e32691764
last_modified_at: 2024-09-19
related_topics:
  - title: English version
    url: /en/common/libreoffice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# libreoffice

Antarmuka baris perintah untuk LibreOffice, aplikasi perkantoran mahir dan gratis.
Informasi lebih lanjut: <https://www.libreoffice.org/>.

- Buka suatu atau beberapa berkas dalam mode baca-saja (read-only):

`libreoffice --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Tampilkan isi suatu atau beberapa berkas:

`libreoffice --cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Cetak berkas menggunakan mesin pencetak (printer) tertentu:

`libreoffice --pt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Konversi semua berkas `.doc` dalam direktori saat ini menuju PDF:

`libreoffice --convert-to pdf *.doc`
