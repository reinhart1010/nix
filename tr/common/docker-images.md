---
layout: page
title: common/docker-images (Türkçe)
description: "Docker imgelerini yönet."
content_hash: 95d0d1eecc0d8deffaa1fd40649836e99a3e564e
related_topics:
  - title: Deutsch version
    url: /de/common/docker-images.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-images.html
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
---
# docker images

Docker imgelerini yönet.
Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/images/>.

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
