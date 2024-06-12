---
layout: page
title: common/ansible-doc (Indonesia)
description: "Tampilkan informasi mengenai modul-modul (action plugins) yang terpasang dalam pustaka pemasangan Ansible."
content_hash: 6d9561c03efdaaf52b70b9afd4c2e7b819c37dc7
last_modified_at: 2024-06-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-doc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-doc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-doc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-doc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ansible-doc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ansible-doc

Tampilkan informasi mengenai modul-modul (action plugins) yang terpasang dalam pustaka pemasangan Ansible.
Tampilkan informasi singkat mengenai daftar plugin beserta deskripsi singkatnya.
Informasi lebih lanjut: <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Tampilkan daftar modul/plugin yang tersedia:

`ansible-doc --list`

- Tampilkan daftar modul/plugin berdasarkan jenisnya:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` --list`

- Tampilkan informasi mengenai suatu modul/plugin:

`ansible-doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_plugin</span>

- Tampilkan informasi mengenai suatu modul/plugin berdasarkan jenis spesifiknya:

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">become|cache|callback|cliconf|connection|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_plugin</span>

- Lihat contoh cara penggunaan (dalam playbook) bagi suatu modul/plugin:

`ansible-doc --snippet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_plugin</span>

- Tampilkan informasi mengenai suatu plugin/modul dalam format JSON:

`ansible-doc --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_plugin</span>
