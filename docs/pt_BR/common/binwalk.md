---
layout: page
title: common/binwalk (português (Brasil))
description: "Ferramenta de análise de Firmware."
content_hash: 6fb25a5952772d800d46918433fae7470a031d45
last_modified_at: 2022-12-27
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># binwalk

Ferramenta de análise de Firmware.
Mais informações: <https://github.com/ReFirmLabs/binwalk>.

- Escaneia um arquivo binário:

`binwalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>

- Extrai arquivos de um binário, especificando a saída do diretório:

`binwalk --extract --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório_do_destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>

- Extrai recursivamente arquivos de um binário limitando a profundidade da recursão para 2:

`binwalk --extract --matryoshka --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>

- Extrai arquivos de um binário com uma assinatura específica:

`binwalk --dd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png image:png</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>

- Analisa a entropia de um binário, salvando o gráfico com o mesmo nome que o binário e a extensão `.png`:

`binwalk --entropy --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>

- Combina entropia, assinatura e análise dos código de operações em um comando só:

`binwalk --entropy --signature --opcodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário</span>
