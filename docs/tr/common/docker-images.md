---
layout: page
title: common/docker-images (Türkçe)
description: "Docker imgelerini yönet."
content_hash: 52946c95b855c1af82299d77033fdf807d0114c2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-images.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-images.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-images.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-images.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-images.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/docker-images.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-images.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker images

Docker imgelerini yönet.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/images/>.

- Tüm Docker imgelerini listele:

`docker images`

- Orta düzeyler de dahil olmak üzere tüm Docker imgelerini sırala:

`docker images --all`

- Çıktıyı sessiz modda (yalnızca sayısal ID'ler olarak) sırala:

`docker images --quiet`

- Herhangi bir konteyner tarafından kullanılmayan tüm Docker imgelerini sırala:

`docker images --filter dangling=true`

- İsminde belirtilen dizeleri taşıyan imgeleri sırala:

`docker images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*isim*</span>`"`
