---
layout: page
title: windows/choco-uninstall (português (Brasil))
description: "Desinstalar um pacote ou mais com Chocolatey."
content_hash: 20b6753e1f4bd035f0c24a75c4a7a26bb9a4af3f
last_modified_at: 2023-11-12
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

- Desinstalar um pacote ou mais separado por espaços:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote(s)</span>

- Desinstalar uma versão específica de um pacote:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Confirmar todos prompts automaticamente:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --yes`

- Remover todas dependências ao desinstalar:

`choco uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --remove-dependencies`

- Desinstalar todos os pacotes:

`choco uninstall all`
