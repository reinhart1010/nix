---
layout: page
title: common/ansible-galaxy (Indonesia)
description: "Buat dan atur peran pengguna (role) Ansible."
content_hash: 9ebd673a4fc16b64a10d513945140b577fb2fbad
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-galaxy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-galaxy

Buat dan atur peran pengguna (role) Ansible.
Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Tampilkan daftar peran atau koleksi yang tersedia:

`ansible-galaxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role|collection</span>` list`

- Cari suatu peran berdasarkan nama menggunakan tingkat verbositas tertentu (`-v` harus dimasukkan pada akhir baris perintah):

`ansible-galaxy role search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_peran</span>` -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vvvvv</span>

- Pasang atau bongkar peran-peran pengguna:

`ansible-galaxy role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_peran1 nama_peran2 ...</span>

- Terbitkan sebuah peran baru:

`ansible-galaxy role init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_peran</span>

- Dapatkan informasi mengenai suatu peran:

`ansible-galaxy role info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_peran</span>

- Pasang atau bongkar kumpulan koleksi (collection):

`ansible-galaxy collection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_koleksi1 nama_koleksi1 ...</span>

- Tampilkan bantuan mengenai manajemen peran (role) maupun koleksi (collection):

`ansible-galaxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role|collection</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
