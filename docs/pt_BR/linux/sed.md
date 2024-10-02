---
layout: page
title: linux/sed (português (Brasil))
description: "Edita texto de uma maneira programável."
content_hash: 16207d6c6f284db51d96dd254b898bc9bcc72272
last_modified_at: 2024-10-02
related_topics:
  - title: English version
    url: /en/linux/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sed.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/sed.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sed

Edita texto de uma maneira programável.
Veja também: `awk`, `ed`.
Mais informações: <https://www.gnu.org/software/sed/manual/sed.html>.

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em todas as linhas de entrada e imprime o resultado na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed 's/apple/mango/g'`

- Substitui todas as ocorrências de `apple` (regex estendida) por `APPLE` (regex estendida) em todas as linhas de entrada e imprime o resultado na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -E 's/(apple)/\U\1/g'`

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em um arquivo específico e sobrescreve o arquivo original:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Executa um arquivo de script específico e imprime o resultado na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sed</span>

- Imprime apenas uma primeira linha na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -n '1p'`

- Exclui a primeira linha de um arquivo:

`sed -i 1d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Adiciona uma nova linha na primeira linha de um arquivo:

`sed -i '1i\sua nova linha de texto\' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
