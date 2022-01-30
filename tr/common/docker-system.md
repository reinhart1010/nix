---
layout: page
title: common/docker-system (Türkçe)
description: "Docker verilerini yönet ve sistem bilgisi görüntüle."
content_hash: 24edcf773b02de8535e91f495c8951a8e6f94493
related_topics:
  - title: Deutsch version
    url: /de/common/docker-system.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
---
# docker system

Docker verilerini yönet ve sistem bilgisi görüntüle.
Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/system/>.

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
