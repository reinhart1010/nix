---
layout: page
title: common/git-mv (italiano)
description: "Sposta o rinomina file e aggiorna l'indice Git."
content_hash: 5b2b170bc665073d177cde422ba06f0bef22922f
related_topics:
  - title: English version
    url: /en/common/git-mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-mv.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-mv.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-mv.html
    icon: bi bi-globe
---
# git mv

Sposta o rinomina file e aggiorna l'indice Git.
Maggiori informazioni: <https://git-scm.com/docs/git-mv>.

- Sposta i file nella repository e aggiungi l'operazione al commit successivo:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo/percorso/del/file</span>

- Rinomina i file e aggiungi l'operazione al commit successivo:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_rinominato</span>

- Sposta sovrascrivendo eventuali file esistenti nel percorso di destinazione:

`git mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo/percorso/del/file</span>
