---
layout: page
title: linux/man (português (Portugal))
description: "Formata e exibe páginas do manual."
content_hash: e4f7c461cb1937ddf7f051a7103597d0b6b9dcbb
related_topics:
  - title: English version
    url: /en/linux/man.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/man.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/man.html
    icon: bi bi-globe
---
# man

Formata e exibe páginas do manual.
Mais informações: <https://manned.org/man>.

- Exibe a página do manual para um comando:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Exibe a página do manual para um comando da seção 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Lista todas as seções disponíveis para um comando:

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Exibe o caminho pesquisado para páginas do manual:

`man --path`

- Exibe a localização de uma página do manual em vez da página em si:

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Exibe a página do manual usando uma localização específica:

`man --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localização</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Procura por páginas do manual que contenham uma certa string:

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string_buscada</span>`"`
