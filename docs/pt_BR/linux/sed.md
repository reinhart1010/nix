---
layout: page
title: linux/sed (português (Brasil))
description: "Edita texto de uma maneira programável."
content_hash: dd496f719db8ce6c0acbea1302f9e50f849104a1
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/linux/sed.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sed

Edita texto de uma maneira programável.
Veja também: `awk`, `ed`.
Mais informações: <https://www.gnu.org/software/sed/manual/sed.html>.

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em todas as linhas de entrada e imprime o resultado na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed 's/apple/mango/g'`

- Executa um arquivo de script específico e imprime o resultado na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sed</span>

- Substitui todas as ocorrências de `apple` (regex estendida) por `APPLE` (regex estendida) em todas as linhas de entrada e imprime o resultado na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -E 's/(apple)/\U\1/g'`

- Imprime apenas uma primeira linha na `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -n '1p'`

- Substitui todas as ocorrências de `apple` (regex básica) por `mango` (regex básica) em um arquivo específico e sobrescreve o arquivo original no lugar:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
