---
layout: page
title: osx/defaults (português (Brasil))
description: "Lê e grava a configuração do usuário do macOS para aplicativos."
content_hash: 2abb2ab6f3f4aeeecc65c87f41997f484599100d
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/defaults.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/defaults.html
    icon: bi bi-globe
tldri18n_status: 2
---
# defaults

Lê e grava a configuração do usuário do macOS para aplicativos.
Mais informações: <https://keith.github.io/xcode-man-pages/defaults.1.html>.

- Lê os padrões do sistema para uma opção do aplicativo:

`defaults read "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opção</span>`"`

- Lê os valores padrão para uma opção do aplicativo:

`defaults read -app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opção</span>`"`

- Pesquisa uma palavra-chave em nomes de domínio, chaves, e valores:

`defaults find "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra-chave</span>`"`

- Grava o valor padrão de uma opção do aplicativo:

`defaults write "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opção</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-tipo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Acelera as animações do Mission Control:

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- Exclui todos os padrões de um aplicativo:

`defaults delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicativo</span>`"`
