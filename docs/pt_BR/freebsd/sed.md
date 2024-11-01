---
layout: page
title: freebsd/sed (português (Brasil))
description: "Edita texto de uma maneira programável."
content_hash: 011f5dbf6b8bc748ccc1e864cbb7c6aca9e7c72f
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/freebsd/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edita texto de uma maneira programável.
Veja também: `awk`, `ed`.
Mais informações: <https://www.freebsd.org/cgi/man.cgi?sed>.

- Substitui todas as ocorrências de `maçã` (regex básico) por `manga` (regex básico) em todas as linhas de entrada e imprime o resultado para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed 's/maçã/manga/g'`

- Executa um script específico e imprime o resultado para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sed</span>

- Atrasa a abertura de cada arquivo até que um comando contendo a função ou flag `w` relacionada seja aplicada a linha de entrada:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/script.sed</span>

- Substitui todas as ocorrências de `maçã` (regex extendido) por `MAÇÃ` (regex extendido) em todas as linhas de entrada e imprime o resultado para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -E 's/(maçã)/\U\1/g'`

- Imprime apenas a primeira linha para `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -n '1p'`

- Substitui todas as ocorrências de `maçã` (regex básico) por `manga` (regex básico) em um arquivo específico e sobrescreve o arquivo original no lugar:

`sed -i 's/maçã/manga/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
