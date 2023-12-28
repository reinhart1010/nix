---
layout: page
title: osx/afplay (português (Brasil))
description: "Player de áudio para linha de comando."
content_hash: 4fcaf77cde853524d12bf8d2f86c36442039711c
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/osx/afplay.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/afplay.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afplay

Player de áudio para linha de comando.
Mais informações: <https://ss64.com/osx/afplay.html>.

- Reproduz um arquivo de som (espera até que a reprodução termine):

`afplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reproduz um arquivo de som em velocidade 2x (taxa de reprodução):

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reproduz um arquivo de som em meia velocidade:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Reproduz os N primeiros segundos de um arquivo de som:

`afplay --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
