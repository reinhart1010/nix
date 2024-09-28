---
layout: page
title: linux/unix2mac (Indonesia)
description: "Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format Unix menuju macOS."
content_hash: 86ae2ead354c88ac74e0020f6d48286b1245b270
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/linux/unix2mac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/unix2mac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unix2mac

Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format Unix menuju macOS.
Program ini menggantikan simbol LF menjadi CR.
Lihat juga: `unix2dos`, `dos2unix`, dan `mac2unix`.
Informasi lebih lanjut: <https://manned.org/unix2mac>.

- Ganti format pengakhiran baris teks dan simpan perubahan pada berkas yang sama:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Ganti format namun simpan perubahan sebagai berkas baru:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--newfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_baru</span>

- Tampilkan informasi suatu berkas teks:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--info</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tetap jaga/tambahkan/hapus simbol Byte Order Mark (BOM) saat mengubah isi berkas:

`unix2mac --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
