---
layout: page
title: common/git-rev-list (français)
description: "Liste les révisions (commits) dans l'ordre chronologique inverse."
content_hash: eb9eae75bc10958146b7755eef64f456fab7273e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-rev-list.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rev-list.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-list.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rev-list.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git rev-list

Liste les révisions (commits) dans l'ordre chronologique inverse.
Plus d'informations : <https://git-scm.com/docs/git-rev-list>.

- Lister tout les commits dans la branche courante :

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Lister tout les commits plus récents qu'une date spécifique, sur une branche spécifique :

`git rev-list --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'2019-12-01 00:00:00'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master</span>

- Lister tout les commits de merge depuis un commit spécifique :

`git rev-list --merges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
