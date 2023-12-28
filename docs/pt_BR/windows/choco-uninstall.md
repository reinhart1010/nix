---
layout: page
title: windows/choco-uninstall (português (Brasil))
description: "Desinstalar um pacote ou mais com Chocolatey."
content_hash: 7a469b952dba774ab7bd253e04e0701177c8ae81
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-uninstall.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-uninstall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco uninstall

Desinstalar um pacote ou mais com Chocolatey.
Mais informações: <https://chocolatey.org/docs/commands-uninstall>.

- Desinstala um pacote ou mais separado por espaços:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote(s)</span>

- Desinstala uma versão específica de um pacote:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Confirma todos prompts automaticamente:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --yes`

- Remove todas dependências ao desinstalar:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --remove-dependencies`

- Desinstala todos os pacotes:

`choco uninstall all`
