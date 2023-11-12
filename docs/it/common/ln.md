---
layout: page
title: common/ln (italiano)
description: "Crea un collegamento a un file o a una directory."
content_hash: 5b46d7d62da98ab38e20c69452dd1aa82e20140e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ln.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ln

Crea un collegamento a un file o a una directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/ln>.

- Crea un collegamento simbolico a un file (o directory):

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/del/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/collegamento</span>

- Sovrascrivi un collegamento esistente in modo che punti a un nuovo file:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/del/nuovo/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/collegamento</span>

- Crea un collegamento fisico a un file:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/del/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/collegamento</span>
