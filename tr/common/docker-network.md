---
layout: page
title: common/docker-network (Türkçe)
description: "Docker ağları oluştur ve yönet."
content_hash: 39ad621c891bc2d853b66bb24f69c66c06836ce4
related_topics:
  - title: Deutsch version
    url: /de/common/docker-network.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
---
# docker network

Docker ağları oluştur ve yönet.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/network/>.

- docker daemon'daki tüm müsait ve düzenlenmiş ağları sırala:

`docker network ls`

- Kullanıcı tarafından belirtilmiş bir ağ oluştur:

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">driver_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_ismi</span>

- Boşluk ile ayrılmış bir ağ listesinin detaylı bilgisini görüntüle:

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_ismi</span>

- Bir konteyneri isim veya ID kullanarak bir ağa bağla:

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi|ID</span>

- Bir konteyneri bir ağdan çıkar:

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi|ID</span>

- Tüm kullanılmayan (hiçbir konteyner tarafından belirtilmeyen) ağları sil:

`docker network prune`

- Kullanılmayan ağların boşluk ile ayrılmış bir listesini sil:

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ağ_ismi</span>
