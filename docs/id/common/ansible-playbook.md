---
layout: page
title: common/ansible-playbook (Indonesia)
description: "Jalankan kumpulan tugas yang didefinisikan di dalam buku aturan main (playbook), kepada para mesin secara jarak jauh melalui SSH."
content_hash: bc75071b7fe1fa6ae30607b84fdd9ad09f503b3b
last_modified_at: 2024-06-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-playbook.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-playbook.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-playbook.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-playbook.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-playbook

Jalankan kumpulan tugas yang didefinisikan di dalam buku aturan main (playbook), kepada para mesin secara jarak jauh melalui SSH.
Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- Jalankan kumpulan tugas yang didefinisikan dalam buku aturan main (playbook):

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Jalankan kumpulan tugas playbook dengan [i]nventaris mesin secara kustom:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_inventaris</span>

- Jalankan kumpulan tugas playbook dengan variabel [e]kstra sebagaimana didefinisikan dalam barisan perintah (command-line):

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabel1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nilai1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabel2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nilai2</span>`"`

- Jalankan kumpulan tugas playbook dengan variabel [e]kstra sebagaimana didefinisikan di dalam suatu berkas JSON:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">daftar_variabel.json</span>`"`

- Jalankan kumpulan tugas playbook dengan konfigurasi tag tertentu:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag1,tag2</span>

- Jalankan kumpulan tugas playbook, dimulai dari nama tugas spesifik:

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` --start-at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_tugas</span>

- Jalankan kumpulan tugas playbook tanpa melakukan perubahan sebenarnya (dry-run):

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` --check --diff`
