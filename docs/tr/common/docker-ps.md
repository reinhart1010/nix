---
layout: page
title: common/docker-ps (Türkçe)
description: "Docker konteynerlerini sırala."
content_hash: 8dc68b595f15b7c04edac368201349fbde77aaab
last_modified_at: 2024-04-19
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
  - title: Indonesia version
    url: /id/common/docker-ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker ps

Docker konteynerlerini sırala.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Halihazırda çalışan Docker konteynerlerini listele:

`docker ps`

- Tüm (durmuş veya çalışan) Docker konteynerlerini listele:

`docker ps --all`

- En son oluşturulan (durmuş veya çalışan) konteynerleri listele:

`docker ps --latest`

- İsimlerinde belirtilen dizeleri içeren konteynerleri filtrele:

`docker ps --filter="name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>`"`

- Belirtilen imge ile akrabalık taşıyan konteynerleri filtrele:

`docker ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imge</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`"`

- Konteynerleri çıkış durum koduna göre filtrele:

`docker ps --all --filter="exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kod</span>`"`

- Konteynerleri mevcut durumlarına (oluşturulma, çalışma, silinme, durma, çıkma ve ölme) göre sırala:

`docker ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mevcut_durum</span>`"`

- Belirtilmiş bir hacmi gömen veya belirtilmiş bir yola gömülmüş hacmi içeren konteynerleri filtrele:

`docker ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dizin</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
