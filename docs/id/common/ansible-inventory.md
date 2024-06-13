---
layout: page
title: common/ansible-inventory (Indonesia)
description: "Tampilkan dan simpan informasi suatu inventaris Ansible (inventory)."
content_hash: e94fedb754ce44ee2ab5bfd4928aece7d6649980
last_modified_at: 2024-06-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-inventory.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-inventory.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-inventory.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-inventory.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-inventory

Tampilkan dan simpan informasi suatu inventaris Ansible (inventory).
Lihat juga: `ansible`.
Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Tampilkan informasi inventaris default:

`ansible-inventory --list`

- Tampilkan suatu inventaris kustom:

`ansible-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_skrip_atau_direktori</span>

- Tampilkan informasi inventaris default dalam format YAML:

`ansible-inventory --list --yaml`

- Simpan informasi inventaris default ke dalam suatu berkas teks:

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
