---
layout: page
title: common/git-push (Deutsch)
description: "Lade Commits in ein Remote-Repository hoch."
content_hash: 88db912d16e9ab33551b708614c17548feda7fa0
related_topics:
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-push.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git push

Lade Commits in ein Remote-Repository hoch.
Weitere Informationen: <https://git-scm.com/docs/git-push>.

- Sende lokale Änderungen des aktuellen Branches zu seinem entfernten Repository (Remote Branch):

`git push`

- Sende lokale Änderungen des angegebenen Branches zu seinem entfernten Repository:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokaler_branch</span>

- Lade den aktuellen Branch in ein entferntes Repository mit Angabe des Namens des entfernten Branches hoch:

`git push -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_branch</span>

- Lade Änderungen eines bestimmten lokalen Branches zu einem bestimmten entfernten Branch hoch:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokaler_branch</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entfernter_branch</span>

- Lade Änderungen aller lokalen Branches zu ihrem entfernten Repository hoch:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Lösche einen Branch in einem entfernten Repository:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_branch</span>

- Entferne alle remote Branches, welche kein lokales Gegenstück besitzen:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Veröffentliche Tags, welche noch nicht im entfernten Repository vorhanden sind:

`git push --tags`
