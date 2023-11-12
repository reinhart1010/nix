---
layout: page
title: common/docker-system (Türkçe)
description: "Docker verilerini yönet ve sistem bilgisi görüntüle."
content_hash: 44a87dac3c14c8a090970d4efb282dfd4d6b2462
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-system.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-system.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-system.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker system

Docker verilerini yönet ve sistem bilgisi görüntüle.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/system/>.

- Yardım göster:

`docker system`

- Docker disk kullanımını göster:

`docker system df`

- Disk kullanımı üzerine detaylı bilgi göster:

`docker system df --verbose`

- Kullanılmayan veriyi sil:

`docker system prune`

- Kullanılmayan ve geçmişte birden çok kez oluşturulan veriyi sil:

`docker system prune --filter="until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saat</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dakika</span>`m"`

- Docker deamon'dan tam-zamanlı eylemleri görüntüle:

`docker system events`

- Geçerli JSON satırları olarak yayınlanan konteynerleden tam-zamanlı eylemleri göster:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- Sistem bilgisi göster:

`docker system info`
