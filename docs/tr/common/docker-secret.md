---
layout: page
title: common/docker-secret (Türkçe)
description: "Docker swarm sırlarını yönet."
content_hash: 4e3b6d0574dcc997e8cad1b0e50c6bb3f800fa90
related_topics:
  - title: Deutsch version
    url: /de/common/docker-secret.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-secret.html
    icon: bi bi-globe
---
# docker secret

Docker swarm sırlarını yönet.
Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/secret/>.

- stdin'den yeni bir sır yarat:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi</span>` -`

- Bir dosyadan yeni sır oluşturun:

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Tüm sırları sırala:

`docker secret ls`

- Bir veya daha fazla sırra dair detaylı bilgiyi insan dostu bir formatta göster:

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi1 sır_ismi2 ...</span>

- Bir veya daha fazla sırrı sil:

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi1 sır_ismi2 ...</span>
