---
layout: page
title: common/git-archive (italiano)
description: "Crea un archivio dei file nell'albero di lavoro."
content_hash: ff817d25b4abfe2648d73c03fc5700d46c646c31
related_topics:
  - title: Deutsch version
    url: /de/common/git-archive.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-archive.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-archive.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-archive.html
    icon: bi bi-globe
---
# git archive

Crea un archivio dei file nell'albero di lavoro.
Maggiori informazioni: <https://git-scm.com/docs/git-archive>.

- Crea un archivio tar del contenuto in HEAD e stampa il risultato su standard output:

`git archive --verbose HEAD`

- Crea un archivio zip del contenuto in HEAD e stampa il risultato su standard output:

`git archive --verbose --format=zip HEAD`

- Come sopra, ma scrivi l'archivio zip su file:

`git archive --verbose --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.zip</span>` HEAD`

- Crea un archivio tar dell'ultimo commit sul ramo specificato:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Crea un archivio tar del contenuto di una specifica cartella:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/directory</span>

- Anteponi un percorso ad ogni file cosí da archiviarlo in una cartella specifica:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.tar</span>` --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/da/anteporre</span>`/ HEAD`
