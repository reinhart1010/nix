---
layout: page
title: common/podman-ps (português (Brasil))
description: "Listar contêineres do Podman."
content_hash: 51d8a6530b65772fbe9b23a3e279b205de15e3c9
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/podman-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman ps

Listar contêineres do Podman.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- Lista contêineres do Podman em execução atualmente:

`podman ps`

- Lista todos os contêineres do Podman (em execução e parados):

`podman ps --all`

- Mostra o contêiner mais recente criado (inclui todos os estados):

`podman ps --latest`

- Filtra contêineres que contêm uma substring em seus nomes:

`podman ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`"`

- Filtra contêineres que compartilham uma determinada imagem como ancestral:

`podman ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagem</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`"`

- Filtra contêineres pelo código de status de saída:

`podman ps --all --filter "exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código</span>`"`

- Filtra contêineres pelo status (criado, em execução, removendo, pausado, encerrado e morto):

`podman ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">status</span>`"`

- Filtra contêineres que montam um volume específico ou têm um volume montado em um caminho específico:

`podman ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
