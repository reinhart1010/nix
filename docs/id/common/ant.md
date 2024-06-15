---
layout: page
title: common/ant (Indonesia)
description: "Apache Ant: bangun dan atur proyek pengembangan piranti lunak berbasis Java."
content_hash: 45a88cdab460862fb5ed005374f89bd174c6ba55
last_modified_at: 2024-06-15
related_topics:
  - title: Deutsch version
    url: /de/common/ant.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ant.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ant.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ant

Apache Ant: bangun dan atur proyek pengembangan piranti lunak berbasis Java.
Informasi lebih lanjut: <https://ant.apache.org>.

- Bangun suatu proyek Java dengan pengaturan yang didefinisikan dalam `build.xml` (lokasi default):

`ant`

- Bangun proyek menggunakan berkas/[f]ile pengaturan selain `build.xml`:

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">buildfile.xml</span>

- Tampilkan informasi mengenai daftar target pembangunan piranti lunak yang memungkinkan bagi proyek ini:

`ant -p`

- Tampilkan informasi pendukung awakutu ([d]ebugging):

`ant -d`

- Jalankan pembangunan bagi seluruh target pembangunan yang tidak bergantung kepada target-target yang gagal dibangun:

`ant -k`
