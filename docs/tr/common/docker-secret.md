---
layout: page
title: common/docker-secret (Türkçe)
description: "Docker swarm sırlarını yönet."
content_hash: bee8c79fad3024ca5a2afc430292ab7462501ef1
last_modified_at: 2024-09-26
related_topics:
  - title: Deutsch version
    url: /de/common/docker-secret.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-secret.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-secret.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-secret.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker secret

Docker swarm sırlarını yönet.
Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/secret/>.

- `stdin`'den yeni bir sır yarat:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>` | docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi</span>` -`

- Bir dosyadan yeni sır oluşturun:

`docker secret create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Tüm sırları sırala:

`docker secret ls`

- Bir veya daha fazla sırra dair detaylı bilgiyi insan dostu bir formatta göster:

`docker secret inspect --pretty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi1 sır_ismi2 ...</span>

- Bir veya daha fazla sırrı sil:

`docker secret rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sır_ismi1 sır_ismi2 ...</span>
