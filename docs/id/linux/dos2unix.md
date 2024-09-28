---
layout: page
title: linux/dos2unix (Indonesia)
description: "Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format DOS menuju Unix."
content_hash: 7683ecbbdc1bf105c591bd417d8f80f670737410
last_modified_at: 2024-09-28
related_topics:
  - title: català version
    url: /ca/linux/dos2unix.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dos2unix.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dos2unix.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/dos2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dos2unix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dos2unix

Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format DOS menuju Unix.
Program ini menggantikan simbol CRLF menjadi LF.
Lihat juga: `unix2dos`, `unix2mac`, dan `mac2unix`.
Informasi lebih lanjut: <https://manned.org/dos2unix>.

- Ganti format pengakhiran baris teks dan simpan perubahan pada berkas yang sama:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Ganti format namun simpan perubahan sebagai berkas baru:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_baru</span>

- Tampilkan informasi suatu berkas teks:

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tetap jaga/tambahkan/hapus simbol Byte Order Mark (BOM) saat mengubah isi berkas:

`dos2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
