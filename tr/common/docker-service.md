---
layout: page
title: common/docker-service (Türkçe)
description: "Bir docker daemon'unun üzerindeki servisleri yönet."
content_hash: 6dafde101350c5513f91d13b121475f296195280
related_topics:
  - title: Deutsch version
    url: /de/common/docker-service.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-service.html
    icon: bi bi-globe
---
# docker service

Bir docker daemon'unun üzerindeki servisleri yönet.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/service/>.

- Bir docker daeomon'unun üzerindeki servisleri listele:

`docker service ls`

- Yeni bir servis yarat:

`docker service create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiket</span>

- Boşluk ile ayrılmış bir servis listesinin detaylı bilgisini görüntüle:

`docker service inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi|ID</span>

- Boşluk ile ayrılmış bir servis listesinin görevlerini sırala:

`docker service ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi|ID</span>

- Boşluk ile ayrılmış bir servis listesi için belirli bir replika miktarına yüksel:

`docker service scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replika_miktarı</span>

- Boşluk ile ayrılmış bir servis listesini sil:

`docker service rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servis_ismi|ID</span>
