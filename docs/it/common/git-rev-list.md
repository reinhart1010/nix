---
layout: page
title: common/git-rev-list (italiano)
description: "Elenca le revisioni (commit) in ordine cronologico inverso."
content_hash: f7d7063e023992fc383782a37a9b92fa8cfd9450
related_topics:
  - title: English version
    url: /en/common/git-rev-list.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rev-list.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-list.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-rev-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git rev-list

Elenca le revisioni (commit) in ordine cronologico inverso.
Maggiori informazioni: <https://git-scm.com/docs/git-rev-list>.

- Mostra tutti i commit del ramo corrente:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Mostra i commit più recenti di una certa data, su uno specifico ramo:

`git rev-list --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'2019-12-01 00:00:00'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Mostra tutti i commit di unione (merge commit) associati a uno specifico commit:

`git rev-list --merges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
