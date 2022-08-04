---
layout: page
title: common/docker-machine (Türkçe)
description: "Docker çalıştıran makineler oluştur ve onları yönet."
content_hash: fed38703fb491db88283086ba0be585a9725be71
related_topics:
  - title: Deutsch version
    url: /de/common/docker-machine.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-machine.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-machine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-machine.html
    icon: bi bi-globe
---
# docker-machine

Docker çalıştıran makineler oluştur ve onları yönet.
Daha fazla bilgi: <https://docs.docker.com/machine/reference/>.

- Halihazırda çalışan docker makinelerini sırala:

`docker-machine ls`

- Belirli bir isim ile docker makinesi oluştur:

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makinenin durumunu öğren:

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makineyi başlat:

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makineyi durdur:

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makine hakkındaki bilgileri incele:

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>
