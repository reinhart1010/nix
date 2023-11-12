---
layout: page
title: common/podman-build (português (Brasil))
description: "Ferramenta sem daemon para criar imagens de contêiner."
content_hash: e6096082b7289dc67d99e57f422fdd8692e8e9e4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/podman-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman build

Ferramenta sem daemon para criar imagens de contêiner.
O Podman fornece uma linha de comando comparável ao Docker-CLI. Simplificando: `alias docker=podman`.
Mais informações: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Criar uma imagem usando um `Dockerfile` ou `Containerfile` no diretório especificado:

`podman build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Criar uma imagem com uma tag especificada:

`podman build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_imagem:versão</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Criar uma imagem a partir de um arquivo não padrão:

`podman build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Containerfile.diferente</span>` .`

- Criar uma imagem sem usar nenhuma imagem em cache previamente:

`podman build --no-cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Criar uma imagem suprimindo todas as saídas:

`podman build --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
