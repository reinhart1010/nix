---
layout: page
title: common/git-bulk (Indonesia)
description: "Lakukan operasi yang sama dalam lebih dari satu repositori Git."
content_hash: 098cbccbb106931561201c23f5f19b7001854ac7
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/git-bulk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-bulk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git bulk

Lakukan operasi yang sama dalam lebih dari satu repositori Git.
Bagian dari `git-extras`.
Informasi lebih lanjut:  <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- Daftarkan direktori saat ini sebagai tempat kerja (workspace):

`git bulk --addcurrent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>

- Masukkan tempat kerja saat ini ke dalam daftar direktori yang akan diubah:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/absolut/menuju/repositori</span>

- Gandakan sebuah repositori ke dalam direktori induk tertentu, kemudian masukkan repositori baru tersebut sebagai tempat kerja:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/absolut/menuju/direktori_induk</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>

- Gandakan lebih dari satu repositori ke dalam direktori induk tertentu (menurut berkas daftar lokasi remote yang dipisah dengan barisan baru), kemudian masukkan sebagai tempat kerja:

`git bulk --addworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/absolut/menuju/direktori_induk</span>` --from {/jalan/absolut/menuju/berkas</span>

- Hapus suatu tempat dari daftar tempat kerja (hal ini tidak akan menghilangkan seluruh isi direktori yang direferensikan sebagai tempat kerja):

`git bulk --removeworkspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_workspace</span>

- Hapus seluruh tempat dari daftar tempat kerja:

`git bulk --purge`
