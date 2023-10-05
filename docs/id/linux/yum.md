---
layout: page
title: linux/yum (Indonesia)
description: "Utilitas manajemen paket untuk RHEL, Fedora, dan CentOS (untuk versi-versi yang lebih lama)."
content_hash: 19499dcafb134bdc7e2f857828668d1f908bc082
last_modified_at: 2023-10-05
related_topics:
  - title: català version
    url: /ca/linux/yum.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/yum.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yum.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yum

Utilitas manajemen paket untuk RHEL, Fedora, dan CentOS (untuk versi-versi yang lebih lama).
Untuk perintah-perintah setara dalam pengelola paket lainnya, lihat <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Informasi lebih lanjut: <https://manned.org/yum>.

- Instal sebuah paket baru

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Instal sebuah paket baru dan mengasumsikan jawaban [y]a untuk semua pertanyaan (juga berfungsi dengan perintah pembaruan, sangat berguna untuk pembaruan otomatis):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Cari sebuah paket yang menyediakan suatu perintah tertentu:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Hapus paket yang terpasang sebelumnya:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Tampilkan pembaruan yang tersedia untuk paket yang terpasang:

`yum check-update`

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`yum upgrade`
