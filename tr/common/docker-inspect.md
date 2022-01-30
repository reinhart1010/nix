---
layout: page
title: common/docker-inspect (Türkçe)
description: "Docker objelerinde bulunan düşük seviye bilgiyi gösterir."
content_hash: 37a7fd6ae09496b8130e00b0132e266264430e2c
related_topics:
  - title: Deutsch version
    url: /de/common/docker-inspect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-inspect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-inspect.html
    icon: bi bi-globe
---
# docker inspect

Docker objelerinde bulunan düşük seviye bilgiyi gösterir.
Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Yardım içeriğini göster:

`docker inspect`

- Bir konteyner, imge veya hacim ile ilgili bilgiyi ismini veya ID'sini girerek görüntüle:

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner|imge|ID</span>

- Bir konteynerin IP adresini görüntüle:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range .NetworkSettings.Networks</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.IPAddress</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner</span>

- Konteynerin log dosyasının yolunu görüntüle:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.LogPath</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner</span>

- Konteynerin imge ismini görüntüle:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Config.Image</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner</span>

- Konfigürasyon bilgisini JSON olarak görüntüle:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .Config</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner</span>

- Tüm port limanlayıcıları görüntüle:

`docker inspect --format='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">range $p, $conf := .NetworkSettings.Ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$p</span>` -> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(index $conf 0).HostPort</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner</span>
