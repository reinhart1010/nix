---
layout: page
title: common/git-bisect (italiano)
description: "Usa la ricerca binaria per trovare il commit che ha introdotto un bug."
content_hash: e0a5e2a27cf10b48a0803c5fa2666c6427bd9c4d
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bisect.html
    icon: bi bi-globe
---
# git bisect

Usa la ricerca binaria per trovare il commit che ha introdotto un bug.
Git salta automaticamente avanti ed indietro nell'albero dei commit per restringere progressivamente il campo fino al commit colpevole.
Maggiori informazioni: <https://git-scm.com/docs/git-bisect>.

- Avvia una ricerca su un intervallo di commit definito dal commit "cattivo" contenente il bug ed un altro commit "buono" privo del bug (solitamente più vecchio):

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_cattivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_buono</span>

- Contrassegna ogni commit selezionato da `git bisect` come "bad" (cattivo) o "good" (buono) dopo averlo testato per verificare la presenza del bug:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- Una volta che `git bisect` ha individuato il commit che ha introdotto il bug, termina la sessione di ricerca e torna al ramo precedente:

`git bisect reset`

- Ignora un commit durante la ricerca (ad esempio uno che fallisce i test per un motivo diverso dal bug ricercato):

`git bisect skip`
