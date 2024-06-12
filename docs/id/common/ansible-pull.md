---
layout: page
title: common/ansible-pull (Indonesia)
description: "Tarik buku-buku aturan main (playbook) dari suatu repositori sistem manajemen versi (VCS), dan jalankan tugas-tugasnya bagi host lokal."
content_hash: 99832e76733e66d033a7ca165fd67b9f2863f22d
last_modified_at: 2024-06-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-pull.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ansible-pull.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ansible-pull

Tarik buku-buku aturan main (playbook) dari suatu repositori sistem manajemen versi (VCS), dan jalankan tugas-tugasnya bagi host lokal.
Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Tarik suatu playbook dari repositori VCS, kemudian jalankan aturan default dari playbook local.yml:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositori</span>

- Tarik suatu playbook dari repositori VCS, kemudian jalankan aturan playbook dengan nama tertentu:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositori</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Tarik suatu playbook dari [C]abang tertentu pada repositori VCS, kemudian jalankan aturan playbook dengan nama tertentu:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositori</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cabang</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Tarik suatu playbook dari repositori VCS, kemudian definisikan daftar perangkat/host dari suatu berkas (hosts), kemudian jalankan aturan playbook dengan nama tertentu:

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_repositori</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_hosts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>
