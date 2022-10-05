---
layout: page
title: common/htop (português (Brasil))
description: "Visualizar informação dinâmica em tempo real acerca de processos em execução. Uma versão melhorada do comando `top`."
content_hash: 577333bf3c2add74a28eedfc86dc94d5e5488fdc
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
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/htop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># htop

Visualizar informação dinâmica em tempo real acerca de processos em execução. Uma versão melhorada do comando `top`.
Mais informações: <https://htop.dev/>.

- Inicializa htop:

`htop`

- Inicializa htop mostrando somente processos pertencentes a um usuário:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_usuário</span>

- Ordena processos por um `item_de_ordenacao` (utilize `htop --sort help` para ver as opçōes disponíveis):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_de_ordenacao</span>

- Vê comandos interativos enquanto roda `htop`:

`?`

- Muda para uma aba diferente:

`tab`

- Mostra ajuda:

`htop --help`
