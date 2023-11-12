---
layout: page
title: common/cowsay (italiano)
description: "Genera un personaggio ASCII (di default una mucca) che dice o pensa qualcosa."
content_hash: 8301b908bc9939155b32fd6c86230c1a10bd83ee
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cowsay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cowsay.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cowsay

Genera un personaggio ASCII (di default una mucca) che dice o pensa qualcosa.
Maggiori informazioni: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Stampa una mucca ASCII che dice "Hello world":

`cowsay "Hello world"`

- Usa il testo da standard input per il fumetto:

`echo "Ciao" | cowsay`

- Elenca tutti i personaggi disponibili:

`cowsay -l`

- Stampa un drago ASCII che dice "Ciao":

`cowsay -f dragon "Ciao"`

- Stampa una mucca ASCII sballata che pensa:

`cowthink -s "Sono solo una mucca, non un grande pensatore..."`
