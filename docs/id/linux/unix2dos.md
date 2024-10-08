---
layout: page
title: linux/unix2dos (Indonesia)
description: "Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format Unix menuju DOS."
content_hash: a92834f00854914dcc6a53641a2ba2d630f9f177
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/linux/unix2dos.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/unix2dos.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2dos

Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format Unix menuju DOS.
Program ini menggantikan simbol LF menjadi CRLF.
Lihat juga: `unix2mac`, `dos2unix`, dan `mac2unix`.
Informasi lebih lanjut: <https://manned.org/unix2dos>.

- Ganti format pengakhiran baris teks dan simpan perubahan pada berkas yang sama:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Ganti format namun simpan perubahan sebagai berkas baru:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_baru</span>

- Tampilkan informasi suatu berkas teks:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tetap jaga/tambahkan/hapus simbol Byte Order Mark (BOM) saat mengubah isi berkas:

`unix2dos --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
