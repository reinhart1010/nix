---
layout: page
title: common/esbuild (português (Brasil))
description: "Empacotador e minificador JavaScript construído para velocidade."
content_hash: d404594c20b4a9289d8037b555335a5c53b1b5d2
related_topics:
  - title: English version
    url: /en/common/esbuild.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># esbuild

Empacotador e minificador JavaScript construído para velocidade.
Mais informações: <https://esbuild.github.io/>.

- Empacota uma aplicação JavaScript e imprime para stdout:

`esbuild --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.js</span>

- Empacota uma aplicação JSX de stdin:

`esbuild --bundle --outfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/saída.js</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.jsx</span>

- Empacota e reduz uma aplicação JSX com mapas de origem no modo `production`:

`esbuild --bundle --define:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process.env.NODE_ENV=\"production\"</span>` --minify --sourcemap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.js</span>

- Empacota uma aplicação JSX para uma lista de navegadores separados por vírgulas:

`esbuild --bundle --minify --sourcemap --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chrome58,firefox57,safari11,edge16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.jsx</span>

- Empacota uma aplicação JavaScript para uma versão específica do node:

`esbuild --bundle --platform=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node</span>` --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node12</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.js</span>

- Empacota uma aplicação JavaScript habilitando a sintaxe JSX em arquivos `.js`:

`esbuild --bundle app.js --loader:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.js=jsx</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.js</span>

- Empacota e serve uma aplicação JavaScript em um servidor HTTP:

`esbuild --bundle --serve=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` --outfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.js</span>

- Empacota uma lista de arquivos em um diretório de saída:

`esbuild --bundle --outdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório_de_saída</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>
