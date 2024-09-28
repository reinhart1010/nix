---
layout: page
title: common/docker-stats (Türkçe)
description: "Konteynerler için kaynak kullanım istatistiklerinin canlı yayınını görüntüle."
content_hash: eb9b436c687f5d81c66a3368cc3969005b3bc7e7
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-stats.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-stats.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-stats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker stats

Konteynerler için kaynak kullanım istatistiklerinin canlı yayınını görüntüle.
Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/stats/>.

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
