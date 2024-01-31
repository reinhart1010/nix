---
layout: page
title: osx/softwareupdate (português (Portugal))
description: "Ferramenta de atualização de aplicativos da App Store via linha de comandos."
content_hash: abd621997a44fa7cdf3772e776c782317bcace1d
last_modified_at: 2024-01-31
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

`softwareupdate --install --req`

- Descarrega e instala um aplicativo específico:

`softwareupdate --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_atulizacao</span>
