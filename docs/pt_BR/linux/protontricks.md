---
layout: page
title: linux/protontricks (português (Brasil))
description: "Um wrapper simples que executa comandos WineTricks para jogos habilitados para o Proton."
content_hash: 07a594af93ee212d7c05fdf207fd840f36607f6a
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/protontricks.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/protontricks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protontricks

Um wrapper simples que executa comandos WineTricks para jogos habilitados para o Proton.
Mais informações: <https://github.com/Matoking/protontricks>.

- Executa a GUI do Protontricks:

`protontricks --gui`

- Executa o WineTricks para um jogo específico:

`protontricks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos_do_winetricks</span>

- Executa um comando no diretório de instalação de um jogo:

`protontricks -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appid</span>

- [l]ista todos os jogos instalados:

`protontricks -l`

- Busca o App ID de um jogo pelo nome:

`protontricks -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_jogo</span>

- Mostra a mensagem de ajuda do Protontricks:

`protontricks --help`
