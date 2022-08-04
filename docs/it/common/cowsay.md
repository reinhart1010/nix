---
layout: page
title: common/cowsay (italiano)
description: "Genera un personaggio ASCII (di default una mucca) che dice o pensa qualcosa."
content_hash: 8301b908bc9939155b32fd6c86230c1a10bd83ee
related_topics:
  - title: English version
    url: /en/common/cowsay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cowsay.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cowsay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
