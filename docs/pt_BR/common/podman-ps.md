---
layout: page
title: common/podman-ps (português (Brasil))
description: "Listar contêineres do Podman."
content_hash: 95487e3bbd5d0dc4c5b433f6270dae4bf2b3a9a9
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/podman-ps.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># podman ps

Listar contêineres do Podman.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- Listar contêineres do Podman em execução atualmente:

`podman ps`

- Listar todos os contêineres do Podman (em execução e parados):

`podman ps --all`

- Mostrar o contêiner mais recente criado (inclui todos os estados):

`podman ps --latest`

- Filtrar contêineres que contenham uma substring em seus nomes:

`podman ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`"`

- Filtrar contêineres que compartilhem uma determinada imagem como ancestral:

`podman ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`"`

- Filtrar contêineres pelo código de status de saída:

`podman ps --all --filter "exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código</span>`"`

- Filtrar contêineres pelo status (criado, em execução, removendo, pausado, encerrado e morto):

`podman ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`"`

- Filtrar contêineres que montam um volume específico ou têm um volume montado em um caminho específico:

`podman ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
