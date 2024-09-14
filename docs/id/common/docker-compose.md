---
layout: page
title: common/docker-compose (Indonesia)
description: "Jalankan dan kelola aplikasi Docker dengan beberapa kontainer."
content_hash: 8a14f9a494d29b03e3a788e78c9bff3117638b06
last_modified_at: 2024-09-14
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker compose

Jalankan dan kelola aplikasi Docker dengan beberapa kontainer.
Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/compose/>.

- Tampilkan semua kontainer yang sedang berjalan:

`docker compose ps`

- Buat dan nyalakan semua kontainer di latar belakang menggunakan file docker-compose.yml dari direktori saat ini:

`docker compose up --detach`

- Nyalakan semua kontainer, dan bangun ulang jika diperlukan:

`docker compose up --build`

- Nyalakan semua kontainer dengan menentukan nama proyek dan menggunakan file compose alternatif:

`docker compose -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_proyek</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>` up`

- Hentikan semua kontainer yang sedang berjalan:

`docker compose stop`

- Hentikan dan menghapus semua kontainer, jaringan, image, dan volume:

`docker compose down --rmi all --volumes`

- Ikuti log untuk semua kontainer:

`docker compose logs --follow`

- Ikuti log untuk kontainer tertentu:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
