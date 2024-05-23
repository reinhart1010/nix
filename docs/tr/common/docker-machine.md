---
layout: page
title: common/docker-machine (Türkçe)
description: "Docker çalıştıran makineler oluştur ve onları yönet."
content_hash: 649a550f12ffc23383850b15948b76b244b85d6a
last_modified_at: 2024-05-23
related_topics:
  - title: Deutsch version
    url: /de/common/docker-machine.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-machine.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-machine.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-machine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-machine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-machine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-machine

Docker çalıştıran makineler oluştur ve onları yönet.
Daha fazla bilgi için: <https://github.com/docker/machine>.

- Halihazırda çalışan Docker makinelerini sırala:

`docker-machine ls`

- Belirli bir isim ile Docker makinesi oluştur:

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makinenin durumunu öğren:

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makineyi başlat:

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makineyi durdur:

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>

- Bir makine hakkındaki bilgileri incele:

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim</span>
