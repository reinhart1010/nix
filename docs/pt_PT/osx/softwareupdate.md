---
layout: page
title: osx/softwareupdate (português (Portugal))
description: "Ferramenta de atualização de aplicativos da App Store via linha de comandos."
content_hash: 33913aae9710a5d92ce484866f3ec96ec9b04831
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/osx/softwareupdate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/softwareupdate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# softwareupdate

Ferramenta de atualização de aplicativos da App Store via linha de comandos.
Mais informações: <https://keith.github.io/xcode-man-pages/softwareupdate.8.html>.

- Lista todos as atualizações disponíveis:

`softwareupdate --list`

- Descarrega e instala todas as atualizações disponíveis:

`softwareupdate --install --all`

- Descarrega e instala todas as atualizações recomendadas:

`softwareupdate --install --recommended`

- Descarrega e instala um aplicativo específico:

`softwareupdate --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_atulizacao</span>
