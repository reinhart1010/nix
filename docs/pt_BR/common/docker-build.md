---
layout: page
title: common/docker-build (português (Brasil))
description: "Cria uma imagem a partir de um Dockerfile."
content_hash: 3367b1c6302126d17bf3078240a669b96b548129
last_modified_at: 2024-03-14
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
  - title: Türkçe version
    url: /tr/common/docker-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker build

Cria uma imagem a partir de um Dockerfile.
Mais informações: <https://docs.docker.com/engine/reference/commandline/build/>.

- Cria uma imagem Docker usando o Dockerfile no diretório atual:

`docker build .`

- Cria uma imagem Docker a partir de um Dockerfile em uma URL específica:

`docker build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github.com/creack/docker-firefox</span>

- Cria uma imagem Docker e cria uma etiqueta para ela:

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome:etiqueta</span>` .`

- Cria uma imagem Docker sem contexto de criação:

`docker build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome:etiqueta</span>` - < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>

- Não usa o cache na criação da imagem:

`docker build --no-cache --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome:etiqueta</span>` .`

- Cria uma imagem Docker usando um Dockerfile específico:

`docker build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dockerfile</span>` .`

- Cria uma imagem Docker utilizando variáveis customizadas para a criação de imagens:

`docker build --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PROXY_DO_HTTP=http://10.20.30.2:1234</span>` --build-arg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PROXY_DO_FTP=http://40.50.60.5:4567</span>` .`
