---
layout: page
title: common/git-svn (italiano)
description: "Operazioni bidirezionali tra repository Subversion e Git."
content_hash: 98b67ca60050d0956293addc09841d8ab581d204
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-svn.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-svn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git svn

Operazioni bidirezionali tra repository Subversion e Git.
Maggiori informazioni: <https://git-scm.com/docs/git-svn>.

- Clona un repository SVN:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://esempio.com/repo_subversion</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory_locale</span>

- Clona un repository SVN a partire da uno specifico numero di revisione:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--revision</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>`:HEAD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://svn.esempio.net/subversion/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory_locale</span>

- Aggiorna una copia locale da un repository SVN remoto:

`git svn rebase`

- Scarica aggiornamenti da un repository SVN remoto senza spostare l'HEAD Git:

`git svn fetch`

- Invia un commit a un repository SVN:

`git svn commit`
