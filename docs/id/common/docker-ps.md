---
layout: page
title: common/docker-ps (Indonesia)
description: "Tampilkan daftar kontainer Docker."
content_hash: 5fd9da24c4ce5c0b7649b4c26b4a0521288d0801
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/docker-ps.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-ps.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-ps.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker ps

Tampilkan daftar kontainer Docker.
Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Tampilkan kontainer Docker yang sedang berjalan saat ini:

`docker ps`

- Tampilkan semua kontainer Docker (yang berjalan dan yang berhenti):

`docker ps --all`

- Tampilkan kontainer yang dibuat terakhir (termasuk semua status):

`docker ps --latest`

- Pilah kontainer yang mengandung substring dalam namanya:

`docker ps --filter="name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>`"`

- Pilah kontainer yang memiliki gambar yang sama sebagai leluhur:

`docker ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`"`

- Pilah kontainer berdasarkan kode status keluar (exit status code):

`docker ps --all --filter="exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode</span>`"`

- Pilah kontainer berdasarkan status (created, running, removing, paused, exited, dan dead):

`docker ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`"`

- Pilah kontainer yang mengaitkan suatu volume tertentu atau memiliki volume yang terpasang pada jalur tertentu:

`docker ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
