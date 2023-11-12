---
layout: page
title: linux/yum (Indonesia)
description: "Utilitas manajemen paket untuk RHEL, Fedora, dan CentOS (untuk versi-versi yang lebih lama)."
content_hash: 47ce879fa642a69422e04a7366fca58192572dac
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# yum

Utilitas manajemen paket untuk RHEL, Fedora, dan CentOS (untuk versi-versi yang lebih lama).
Untuk perintah-perintah setara dalam pengelola paket lainnya, lihat <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Informasi lebih lanjut: <https://manned.org/yum>.

- Instal sebuah paket baru:

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
