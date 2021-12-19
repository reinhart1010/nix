---
layout: page
title: common/flake8 (italiano)
description: "Programma per verificare lo stile e la qualità di un codice Python."
content_hash: 2eced5d970f5b62163765426b45d0cf44cdf91a5
related_topics:
  - title: English version
    url: /en/common/flake8.html
    icon: bi bi-globe
---
# flake8

Programma per verificare lo stile e la qualità di un codice Python.
Maggiori informazioni: <https://flake8.pycqa.org/>.

- Analizza ricorsivamente un file o una cartella:

`flake8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Analizza ricorsivamente un file o una cartella e mostra le righe contenenti errori:

`flake8 --show-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Analizza ricorsivamente un file o una cartella e ignora la lista delle regole specificate. (La lista con tutte le regole è consultabile su flake8rules.com):

`flake8 --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regola1,regola2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>

- Analizza ricorsivamente un file o una cartella ma esclude i file che corrispondono a una sottostringa o a un glob:

`flake8 --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sottostringa1,glob2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_cartella</span>
