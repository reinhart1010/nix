---
layout: page
title: windows/choco-source (português (Brasil))
description: "Gerenciar fontes para pacotes com Chocolatey."
content_hash: 54a0fa2e6b81a84ffa14c28f85c3dda8812c70d3
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-source.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-source.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-source.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-source.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-source.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-source.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco source

Gerenciar fontes para pacotes com Chocolatey.
Mais informações: <https://chocolatey.org/docs/commands-source>.

- Listar fontes atualmente disponíveis:

`choco source list`

- Adicionar uma nova fonte de pacotes:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_da_fonte</span>

- Adicionar uma nova fonte de pacotes com credenciais:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_da_fonte</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>

- Adicionar uma nova fonte de pacotes com certificado do cliente:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_da_fonte</span>` --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/certificado</span>

- Habilitar uma fonte de pacotes:

`choco source enable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Desabilitar uma fonte de pacotes:

`choco source disable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Remover uma fonte de pacotes:

`choco source remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
