---
layout: page
title: linux/pacman4console (português (Brasil))
description: "Um jogo de console baseado em texto inspirado no Pacman original."
content_hash: dc240c983a126b0dc2881c7d72cc7d6d91e1c51b
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/pacman4console.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman4console.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman4console.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman4console

Um jogo de console baseado em texto inspirado no Pacman original.
Mais informações: <https://github.com/YoctoForBeaglebone/pacman4console>.

- Inicia um jogo no nível 1:

`pacman4console`

- Inicia um jogo em determinado nível (há nove níveis oficiais):

`pacman4console --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_nivel</span>

- Inicia o editor de níveis do pacman4console, salvando em um arquivo texto especificado:

`pacman4consoleedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_nivel</span>

- Joga um nível personalizado:

`pacman4console --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_nivel</span>
