---
layout: page
title: common/git-difftool (italiano)
description: "Mostra le modifiche ai file tracciati usando uno strumento Diff esterno. Accetta le stesse opzioni e argomenti di Git diff."
content_hash: d66f11605e716572ba300b84a96664ed78fd063c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-difftool.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-difftool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-difftool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git difftool

Mostra le modifiche ai file tracciati usando uno strumento Diff esterno. Accetta le stesse opzioni e argomenti di Git diff.
Maggiori informazioni: <https://git-scm.com/docs/git-difftool>.

- Elenca gli strumenti Diff disponibili:

`git difftool --tool-help`

- Imposta meld come strumento Diff predefinito:

`git config --global diff.tool "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meld</span>`"`

- Usa lo strumento Diff predefinito per mostrare le modifiche nell'area di stage:

`git difftool --staged`

- Uso uno specifico strumento Diff (opendiff) per mostrare le modifiche a partire da un dato commit:

`git difftool --tool=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opendiff</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
