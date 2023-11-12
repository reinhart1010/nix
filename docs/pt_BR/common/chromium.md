---
layout: page
title: common/chromium (português (Brasil))
description: "Navegador código aberto do Google."
content_hash: a8ffd3262c65508ef50de5e95f6143386c5de799
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/chromium.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chromium.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chromium.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chromium.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chromium.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chromium

Navegador código aberto do Google.
Mais informações: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Abre um arquivo:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.html</span>

- Abre uma URL:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre no modo de navegação anônima (icognito):

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre em uma nova janela:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre no modo app (Sem barra de tarefas, barra de URL, botões, etc.):

`chromium --app='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>`'`

- Usa um servidor proxy:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>
