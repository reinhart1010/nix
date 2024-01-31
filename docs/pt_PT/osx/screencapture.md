---
layout: page
title: osx/screencapture (português (Portugal))
description: "Utilitário para fazer capturas de ecrã e gravações de ecrã."
content_hash: c578690022283aff2a4121a7a4d2c23e479476c0
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/screencapture.html
    icon: bi bi-globe
tldri18n_status: 2
---
# screencapture

Utilitário para fazer capturas de ecrã e gravações de ecrã.
Mais informações: <https://keith.github.io/xcode-man-pages/screencapture.1.html>.

- Faz um captura de ecrã e guarda-a num ficheiro:

`screencapture `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ficheiro.png</span>

- Faz um captura de ecrã incluindo o curso do rato e guarda-a num ficheiro:

`screencapture -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ficheiro.png</span>

- Faz um captura de ecrã e mostra-a em Pré-visualização, em vez de a guardar:

`screencapture -P`

- Faz uma captura de ecrã de uma área retangular selecionada:

`screencapture -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ficheiro.png</span>

- Faz uma captura de ecrã de uma área depois de um intervalo de tempo:

`screencapture -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ficheiro.png</span>

- Faz uma gravação de ecrã guardando-a para um ficheiro:

`screencapture -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ficheiro.mp4</span>
