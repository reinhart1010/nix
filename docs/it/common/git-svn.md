---
layout: page
title: common/git-svn (italiano)
description: "Operazioni bidirezionali tra repository Subversion e Git."
content_hash: b1040ee4abdd851459e52b23eb46658f42d87154
related_topics:
  - title: English version
    url: /en/common/git-svn.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-svn.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-svn.html
    icon: bi bi-globe
---
# git svn

Operazioni bidirezionali tra repository Subversion e Git.
Maggiori informazioni: <https://git-scm.com/docs/git-svn>.

- Clona un repository SVN:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com/repo_subversion</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cartella_locale</span>

- Clona un repository SVN a partire da uno specifico numero di revisione:

`git svn clone -r`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>`:HEAD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://svn.esempio.net/subversion/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cartella_locale</span>

- Aggiorna una copia locale da un repository SVN remoto:

`git svn rebase`

- Scarica aggiornamenti da un repository SVN remoto senza spostare l'HEAD Git:

`git svn fetch`

- Invia un commit a un repository SVN:

`git svn dcommit`
