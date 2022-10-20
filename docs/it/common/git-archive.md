---
layout: page
title: common/git-archive (italiano)
description: "Crea un archivio dei file nell'albero di lavoro."
content_hash: f655a3284c05bc93c9ac4ac2fc719483104a56b0
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
  - title: Türkçe version
    url: /tr/common/git-archive.html
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

`git archive --verbose --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.zip</span>` HEAD`

- Crea un archivio tar dell'ultimo commit sul ramo specificato:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Crea un archivio tar del contenuto di una specifica directory:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.tar</span>` HEAD:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Anteponi un percorso ad ogni file cosí da archiviarlo in una directory specifica:

`git archive --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.tar</span>` --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/da/anteporre</span>`/ HEAD`
