---
layout: page
title: common/ansible-vault (Indonesia)
description: "Enkripsi dan dekripsi nilai, struktur data, dan file dalam proyek Ansible."
content_hash: 1d8282db7b9547de4c887351efeebffa1bf83900
last_modified_at: 2024-06-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-vault.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-vault.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-vault.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-vault

Enkripsi dan dekripsi nilai, struktur data, dan file dalam proyek Ansible.
Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Buat suatu berkas brankas terenkripsi baru dengan permintaan kata sandi:

`ansible-vault create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_brankas</span>

- Buat file brankas terenkripsi baru menggunakan berkas kunci (kata sandi) brankas untuk mengenkripsinya:

`ansible-vault create --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_brankas</span>

- Enkripsi file yang ada menggunakan berkas kata sandi opsional:

`ansible-vault encrypt --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_brankas</span>

- Enkripsi suatu teks string menggunakan format string terenkripsi standar Ansible, dan menampilkan petunjuk secara interaktif:

`ansible-vault encrypt_string`

- Lihat isi suatu brankas yang terenkripsi, menggunakan berkas kata sandi untuk mendekripsikannya:

`ansible-vault view --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_brankas</span>

- Ganti kunci (kata sandi) pada brankas terenkripsi dengan mendefinisikan berkas kata sandi baru:

`ansible-vault rekey --vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_kata_sandi_lama</span>` --new-vault-password-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_kata_sandi_baru</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_brankas</span>
