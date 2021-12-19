---
layout: page
title: common/docker-swarm (Türkçe)
description: "Bir konteyner orkestrasyon aracı."
content_hash: 038a385efeed5cee4b5803047b1f76399047ebd9
related_topics:
  - title: Deutsch version
    url: /de/common/docker-swarm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-swarm.html
    icon: bi bi-globe
---
# docker swarm

Bir konteyner orkestrasyon aracı.
Daha fazla bilgi için: <https://docs.docker.com/engine/swarm/>.

- Bir bataklık dizisi oluştur:

`docker swarm init`

- Bir yönetici veya işçiye takılmak için token göster:

`docker swarm join-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">işçi|yönetici</span>

- Diziye yeni bir düğüm ekle:

`docker swarm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manager_node_url:2377</span>

- Bir işçiyi bataklıktan sil (işçi düğümünün içinde çalıştır):

`docker swarm leave`

- Mevcut CA sertifikasını PEM formatında görüntüle:

`docker swarm ca`

- Mevcut CA sertifikasını döndür ve yeni sertifikayı görüntüle:

`docker swarm ca --rotate`

- Düğüm sertifikaları için geçerli periyodu değiştir:

`docker swarm update --cert-expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saat</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dakika</span>`m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saniye</span>`s`
