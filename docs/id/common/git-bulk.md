---
layout: page
title: common/git-bulk (Indonesia)
description: "Lakukan operasi yang sama dalam lebih dari satu repositori Git."
content_hash: 114dab85a0f7bedd600dc9d673fe0b8d97e5bfb2
last_modified_at: 2024-09-11
related_topics:
  - title: English version
    url: /en/common/git-bulk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bulk

Lakukan operasi yang sama dalam lebih dari satu repositori Git.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- Daftarkan direktori saat ini sebagai tempat kerja (workspace):

`git bulk --addcurrent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>

- Masukkan tempat kerja saat ini ke dalam daftar direktori yang akan diubah:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/absolut/menuju/repositori</span>

- Gandakan suatu repositori ke dalam direktori induk tertentu, kemudian masukkan repositori baru tersebut sebagai tempat kerja:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/absolut/menuju/direktori_induk</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>

- Gandakan lebih dari satu repositori ke dalam direktori induk tertentu (menurut berkas daftar lokasi remote yang dipisah dengan barisan baru), kemudian masukkan sebagai tempat kerja:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/absolut/menuju/direktori_induk</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/absolut/menuju/berkas</span>

- Tampilkan daftar seluruh tempat kerja yang terdaftar:

`git bulk --listall`

- Jalankan sebuah perintah Git pada kumpulan repositori yang dikelola oleh tempat kerja saat ini:

`git bulk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumen-argumen_perintah</span>

- Hapus suatu tempat dari daftar tempat kerja (hal ini tidak akan menghilangkan seluruh isi direktori yang direferensikan sebagai tempat kerja):

`git bulk --removeworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>

- Hapus seluruh tempat dari daftar tempat kerja:

`git bulk --purge`
