---
layout: page
title: common/docker-service (Türkçe)
description: "Bir Docker daemon'unun üzerindeki servisleri yönet."
content_hash: 5647172bc0bbc107b8c15f38b113ede24108a786
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/docker-service.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-service.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-service.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker service

Bir Docker daemon'unun üzerindeki servisleri yönet.
Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/service/>.

- Bir Docker daeomon'unun üzerindeki servisleri listele:

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
