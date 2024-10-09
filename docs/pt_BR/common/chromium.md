---
layout: page
title: common/chromium (português (Brasil))
description: "Navegador web de código aberto desenvolvido e mantido principalmente pela Google."
content_hash: c91907402215d78ce68ae6075a331aa0b6d655a5
last_modified_at: 2024-10-09
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

Navegador web de código aberto desenvolvido e mantido principalmente pela Google.
Mais informações: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Abre uma URL ou arquivo específico:

`chromium `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemplo.com|caminho/para/arquivo.html</span>

- Abre no modo de navegação anônima (incógnito):

`chromium --incognito `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre em uma nova janela:

`chromium --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre no modo aplicativo (sem barra de tarefas, barra de URL, botões, etc.):

`chromium --app=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemplo.com</span>

- Usa um servidor proxy:

`chromium --proxy-server="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">socks5://hostname:66</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Abre com um diretório de perfil customizado:

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Abre sem validação CORS (útil para testar uma API):

`chromium --user-data-dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` --disable-web-security`

- Abre com uma janela DevTools para cada aba aberta:

`chromium --auto-open-devtools-for-tabs`
