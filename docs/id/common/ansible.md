---
layout: page
title: common/ansible (Indonesia)
description: "Atur grup perangkat komputer yang secara jarak jauh melalui SSH. (Gunakan berkas `/etc/ansible/hosts` untuk menambahkan grup atau host baru)."
content_hash: 73840b7a345b44f65df9496e58e5d75698fc36c9
last_modified_at: 2024-06-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ansible.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ansible.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ansible.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ansible

Atur grup perangkat komputer yang secara jarak jauh melalui SSH. (Gunakan berkas `/etc/ansible/hosts` untuk menambahkan grup atau host baru).
Beberapa subperintah seperti `ansible galaxy` memiliki dokumentasi terpisah.
Informasi lebih lanjut: <https://www.ansible.com/>.

- Tampilkan daftar host yang tergabung dalam suatu grup:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup</span>` --list-hosts`

- Uji koneksi (ping) kepada grup perangkat tertentu dengan menggunakan [m]odul ping:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup</span>` -m ping`

- Tampilkan informasi faktual tentang suatu grup perangkat dengan menggunakan [m]odul setup:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup</span>` -m setup`

- Jalankan perintah pada suatu kelompok perangkat melalui [m]odul command dengan kumpulan [a]rgumen:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah_saya</span>`'`

- Jalankan perintah dengan hak akses administratif:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup</span>` --become --ask-become-pass -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah_saya</span>`'`

- Jalankan perintah menggunakan berkas [i]nventaris tertentu:

`ansible `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_inventaris</span>` -m command -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah_saya</span>`'`

- Tampilkan daftar grup dalam sebuah inventaris:

`ansible localhost -m debug -a '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var=groups.keys()</span>`'`
