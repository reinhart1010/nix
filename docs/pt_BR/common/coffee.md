---
layout: page
title: common/coffee (português (Brasil))
description: "Executa scripts CoffeeScript ou os compila em JavaScript."
content_hash: e5e9a0c80d4a51435d0f0aab3dd4f85f3d4d1d3d
last_modified_at: 2023-10-21
related_topics:
  - title: English version
    url: /en/common/coffee.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/coffee.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/coffee.html
    icon: bi bi-globe
---
# coffee

Executa scripts CoffeeScript ou os compila em JavaScript.
Mais informações: <https://coffeescript.org#cli>.

- Executa um script:

`coffee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.coffee</span>

- Compila para JavaScript e salva em um arquivo com o mesmo nome:

`coffee --compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.coffee</span>

- Compila para JavaScript e salva em um arquivo de saída indicado:

`coffee --compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.coffee</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.js</span>

- Inicia um REPL (shell interativo):

`coffee --interactive`

- Observa script para alterações e o executa novamente:

`coffee --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.coffee</span>
