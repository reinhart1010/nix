---
layout: page
title: common/htop (português (Brasil))
description: "Exibe informação dinâmica em tempo real acerca de processos em execução. Uma versão melhorada do comando `top`."
content_hash: 18042afe0af3b44224cbad4b16c7c5c72022ec31
last_modified_at: 2024-07-26
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/htop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/htop.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/htop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/htop.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># htop

Exibe informação dinâmica em tempo real acerca de processos em execução. Uma versão melhorada do comando `top`.
Mais informações: <https://htop.dev/>.

- Inicializa `htop`:

`htop`

- Inicializa `htop` mostrando somente processos pertencentes a um usuário:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_usuário</span>

- Ordena processos por um `item_de_ordenação` (utilize `htop --sort help` para ver as opções disponíveis):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_de_ordenação</span>

- Inicializa `htop` com um atraso especificado entre atualizações, em décimos de segundo (p. ex. 50 = 5 segundos):

`htop --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- Vê comandos interativos enquanto roda `htop`:

`?`

- Muda para uma aba diferente:

`tab`

- Mostra ajuda:

`htop --help`
