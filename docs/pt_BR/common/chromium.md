---
layout: page
title: common/chromium (português (Brasil))
description: "Navegador código aberto desenvolvido principalmente e mantido pela Google."
content_hash: 13ecace443bbb0ea30cc28cf92bc38670d16b16a
last_modified_at: 2024-04-19
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
  - title: Nederlands version
    url: /nl/common/chromium.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chromium

Navegador código aberto desenvolvido principalmente e mantido pela Google.
Mais informações: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Abre uma URL ou arquivo específico:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemplo.com|caminho/para/arquivo.html</span>

- Abre no modo de navegação anônima (incógnito):

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre em uma nova janela:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre no modo aplicativo (Sem barra de tarefas, barra de URL, botões, etc.):

`chromium --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemplo.com</span>

- Usa um servidor proxy:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre com um diretório de perfil customizado:

`chromium --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre sem validação CORS (útil para testar uma API):

`chromium --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` --disable-web-security`

- Abre com uma janela DevTools para cada aba aberta:

`chromium --auto-open-devtools-for-tabs`
