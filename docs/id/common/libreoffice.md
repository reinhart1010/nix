---
layout: page
title: common/libreoffice (Indonesia)
description: "Antarmuka baris perintah untuk LibreOffice, aplikasi perkantoran mahir dan gratis."
content_hash: abc8f8dbb38044d6bba2730cda7743779faf159d
last_modified_at: 2024-09-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/libreoffice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libreoffice

Antarmuka baris perintah untuk LibreOffice, aplikasi perkantoran mahir dan gratis.
Informasi lebih lanjut: <https://www.libreoffice.org/>.

- Buka suatu atau beberapa berkas dalam mode baca-saja (read-only):

`libreoffice --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Tampilkan isi suatu atau beberapa berkas:

`libreoffice --cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Cetak berkas menggunakan mesin pencetak (printer) tertentu:

`libreoffice --pt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Konversi semua berkas `.doc` dalam direktori saat ini menuju PDF:

`libreoffice --convert-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.doc</span>
