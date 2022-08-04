---
layout: page
title: common/firefox (português (Brasil))
description: "Um browser livre e de código aberto."
content_hash: fd5626f99bb17db6ffe1c012d77f160df47408d1
related_topics:
  - title: Deutsch version
    url: /de/common/firefox.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/firefox.html
    icon: bi bi-globe
---
# firefox

Um browser livre e de código aberto.
Mais informações: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- Inicie o Firefox e abra uma página web:

`firefox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- Abra uma nova janela:

`firefox --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- Abra uma janela privativa (incognito):

`firefox --private-window`

- Pesquise por "wikipedia" usando a engine de busca padrão:

`firefox --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wikipedia</span>`"`

- Inicie o Firefox no modo seguro, com todas as extensões desativadas:

`firefox --safe-mode`

- Tire uma screenshot de uma página web no modo headless:

`firefox --headless --screenshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_saida.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemplo.com/</span>

- Use um perfil específico para permitir que múltiplas instâncias separadas do Firefox rodem ao mesmo tempo:

`firefox --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- Configure o Firefox como o navegador padrão:

`firefox --setDefaultBrowser`
