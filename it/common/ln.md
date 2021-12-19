---
layout: page
title: common/ln (italiano)
description: "Crea un collegamento a un file o a una directory."
content_hash: 0d15d48d8e6ce6771f5d9144d90b2d78858119fd
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
---
# ln

Crea un collegamento a un file o a una directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/ln>.

- Crea un collegamento simbolico a un file (o directory):

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/al/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/collegamento</span>

- Sovrascrivi un collegamento esistente in modo che punti a un nuovo file:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/al/nuovo/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/collegamento</span>

- Crea un collegamento fisico a un file:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/al/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/collegamento</span>
