---
layout: page
title: common/docker-logs (Türkçe)
description: "Konteyner kaydını yazdırır."
content_hash: d1caf3dc03b18796217c26ebe6805104b86255eb
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/common/docker-logs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-logs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-logs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-logs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker-logs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker logs

Konteyner kaydını yazdırır.
Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Bir konteyner içindeki kayıtları yazdır:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>

- Kayıtları yazdır ve izle:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>

- Son 5 kaydı yazdır:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` --tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Kayıtları yazdır ve zaman damgaları ile iliştir:

`docker logs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>

- Belli bir konteyner çalışma zamanındaki (i.e. 23m, 10s, 2013-01-02T13:23:37) kayıtları yazdır:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konteyner_ismi</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zaman</span>
