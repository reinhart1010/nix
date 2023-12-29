---
layout: page
title: common/column (italiano)
description: "Formatta standard input o un file in più colonne."
content_hash: dca57e5fd9f97485caaf35b1be902eae0fb909af
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/column.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/column.html
    icon: bi bi-globe
tldri18n_status: 2
---
# column

Formatta standard input o un file in più colonne.
Le colonne sono riempite prima delle righe; il separatore predefinito è lo spazio.
Maggiori informazioni: <https://manned.org/column>.

- Formatta l'output per uno schermo largo 30 caratteri:

`printf "intestazione1 intestazione2\nbar foo\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Separa colonne ed allinea automaticamente in un formato tabulare:

`printf "intestazione1 intestazione2\nbar foo\n" | column --table`

- Specifica un diverso separatore di colonna (e.g. "," per csv) (il predefinito è lo spazio):

`printf "intestazione1 intestazione2\nbar foo\n" | column --table --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Riempi le righe prima delle colonne:

`printf "intestazione1\nbar\nfoobar\n" | column --output-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` --fillrows`
