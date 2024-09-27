---
layout: page
title: linux/mac2unix (Indonesia)
description: "Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format DOS menuju Unix."
content_hash: 9fb59550547aa87d98dbc302475312e4a923368a
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/linux/mac2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mac2unix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mac2unix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mac2unix

Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format DOS menuju Unix.
Program ini menggantikan simbol CRLF menjadi LF.
Lihat juga: `unix2dos`, `unix2mac`, dan `dos2unix`.
Informasi lebih lanjut: <https://manned.org/mac2unix>.

- Ganti format pengakhiran baris teks dan simpan perubahan pada berkas yang sama:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Ganti format namun simpan perubahan sebagai berkas baru:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_baru</span>

- Tampilkan informasi suatu berkas teks:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tetap jaga/tambahkan/hapus simbol Byte Order Mark (BOM) saat mengubah isi berkas:

`mac2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
