---
layout: page
title: common/docker (Indonesia)
description: "Atur kontainer Docker dan image."
content_hash: 6ce428390baf02c6b827defe715be7eddf32a42d
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/docker.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/docker.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/docker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker

Atur kontainer Docker dan image.
Beberapa subperintah seperti `run` mempunyai dokumentasi terpisah.
Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/>.

- Tampilkan semua daftar kontainer Docker (yang sedang berjalan dan berhenti):

`docker ps --all`

- Nyalakan sebuah kontainer dari citra (image), dengan nama kustom:

`docker run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_kontainer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">citra</span>

- Nyalakan atau menghentikan kontainer yang tersedia:

`docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_kontainer</span>

- Tarik citra dari registri Docker:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">citra</span>

- Tampilkan daftar citra Docker yang telah diunduh:

`docker images`

- Buka sesi shell didalam sebuah kontainer yang sedang berjalan:

`docker exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_kontainer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- Hapus kontainer yang sedang berhenti:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_kontainer</span>

- Ambil dan ikuti semua log dari sebuah kontainer:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_kontainer</span>
