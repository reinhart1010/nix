---
layout: page
title: common/docker-build (Türkçe)
description: "Bir Dockerfile'dan imge yaratın."
content_hash: 247fd84aafebc11a5a985e1300793390897aa31b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-build.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-build.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-build.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-build.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-build.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-build.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-build.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker build

Bir Dockerfile'dan imge yaratın.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/build/>.

- Mevcut dizindeki Dockerfile'dan bir docker imgesi oluşturun:

`docker build .`

- Belirtilen URL'deki Dockerfile'dan bir docker imgesi oluşturun:

`docker build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ornekadres.com/ornek-dizin/ornek-docker-projesi</span>

- Bir docker imgesi oluşturun ve etiketleyin:

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim:etiket</span>` .`

- İmge oluştururken çerez kullanımını etkisizleştirin:

`docker build --no-cache --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">isim:etiket</span>` .`

- Belirtilen Dockerfile ile bir docker imgesi oluşturun:

`docker build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>` .`

- Kişiselleştirilmiş yapım-zaman değerleriyle oluşturun:

`docker build --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HTTP_PROXY=http://10.20.30.2:1234</span>` --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FTP_PROXY=http://40.50.60.5:4567</span>` .`
