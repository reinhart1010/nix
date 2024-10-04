---
layout: page
title: osx/xcodes-runtimes (português (Brasil))
description: "Gerencia runtimes do Simulador Xcode."
content_hash: 9a686cada12eee324d2d9d5e978887c61f48d40e
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xcodes-runtimes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/xcodes-runtimes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcodes runtimes

Gerencia runtimes do Simulador Xcode.
Mais informações: <https://github.com/xcodesorg/xcodes>.

- Lista todos os runtimes do Simulador disponíveis:

`xcodes runtimes --include-betas`

- Baixa um runtime do Simulador:

`xcodes runtimes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome-do-runtime</span>

- Baixa e instala um runtime do Simulador:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome-do-runtime</span>

- Baixa/instala um runtime do Simulador para a versão iOS/watchOS/tvOS/visionOS especificada (diferencia maiúsculo de minúsculo):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iOS|watchOS|tvOS|visionOS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão_runtime</span>`"`

- Define um local específico para onde o pacote do runtime será baixado primeiro (o padrão é `~/Downloads`):

`xcodes runtimes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">download|install</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_runtime</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Não exclui o pacote baixado quando o Simulador é instalado com sucesso:

`xcodes runtimes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_runtime</span>` --keep-archive`
