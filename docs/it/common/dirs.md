---
layout: page
title: common/dirs (italiano)
description: "Mostra o manipola uno stack di directory."
content_hash: d24790919b492a6a8e3d62623645803184577b61
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/dirs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dirs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirs

Mostra o manipola uno stack di directory.
Uno stack di directory è una lista di directory recentemente visitate che può essere manipolata con i comandi `pushd` e `popd`.
Maggiori informazioni: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Mostra lo stack di directory dividendo i nomi con uno spazio:

`dirs`

- Mostra lo stack di directory una per riga:

`dirs -p`

- Mostra solo l'ennesima directory dello stack (gli indici partono da 0):

`dirs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- Pulisci lo stack di directory:

`dirs -c`
