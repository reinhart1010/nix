---
layout: page
title: common/docker-stats (Türkçe)
description: "Konteynerler için kaynak kullanım istatistiklerinin canlı yayınını görüntüle."
content_hash: 9c3e651f8afc75f72b8644f6509e83b40f32350c
related_topics:
  - title: Deutsch version
    url: /de/common/docker-stats.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-stats.html
    icon: bi bi-globe
---
# docker stats

Konteynerler için kaynak kullanım istatistiklerinin canlı yayınını görüntüle.
Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Çalışan tüm konteynerlerin aynak kullanım istatistiklerinin canlı yayınını görüntüle:

`docker stats`

- Boşluk ile ayrılmış bir listedeki konteynerlerin canlı yayınını görüntüle:

`docker stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_ismi</span>

- Konteyner'in CPU kullanım yüzdesini göstermek için sütun formatını değiştir:

`docker stats --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Name</span>`:\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.CPUPerc</span>`"`

- Tüm (çalışan veya durmuş) konteynerler için istatistikleri görüntüle:

`docker stats --all`

- İstatistikleri canlı yayınlamayı durdur ve yalnızca mevcut durumdaki istatistikleri görüntüle:

`docker stats --no-stream`
