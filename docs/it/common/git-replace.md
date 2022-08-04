---
layout: page
title: common/git-replace (italiano)
description: "Crea, elenca, ed elimina riferimenti ad oggetti sostituiti."
content_hash: a0f7b65c314cc0035e36a43c523c7e915240b210
related_topics:
  - title: English version
    url: /en/common/git-replace.html
    icon: bi bi-globe
---
# git replace

Crea, elenca, ed elimina riferimenti ad oggetti sostituiti.
Maggiori informazioni: <https://git-scm.com/docs/git-replace>.

- Sostituisci un commit con un altro, senza modificare gli altri commit:

`git replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oggetto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oggetto_sostitutivo</span>

- Cancella riferimenti esistenti ad un oggetto sostituito:

`git replace --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oggetto</span>

- Modifica il contenuto di un oggetto in modo interattivo:

`git replace --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oggetto</span>
