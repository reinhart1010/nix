---
layout: page
title: common/docker-start (Türkçe)
description: "Bir veya daha fazla durmuş konteyneri başlar."
content_hash: ae61267e4b955f505f2fa627b3b522575eaed05a
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/docker-start.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-start.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-start.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-start.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-start.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker start

Bir veya daha fazla durmuş konteyneri başlar.
Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/start/>.

- Yardım göster:

`docker start`

- Bir Docker konteynerini başlat:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner</span>

- Bir konteyneri, ona `stdout` ile `stderr`'i ekleyerek ve sinyaller göndererek başlat:

`docker start --attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner</span>

- Bir veya daha fazla boşlukla ayrılarak belirtilmiş konteynerleri başlar:

`docker start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner1 konteyner2 ...</span>
