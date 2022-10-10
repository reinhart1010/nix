---
layout: page
title: common/git-bisect (Deutsch)
description: "Benutzt binäre Suche um den commit ausfindig zu machen, welcher einen Fehler beinhaltet."
content_hash: 901c43c3b8d06dfa3fc0c79b52f6142082db94be
related_topics:
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bisect.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bisect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bisect.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-bisect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git bisect

Benutzt binäre Suche um den commit ausfindig zu machen, welcher einen Fehler beinhaltet.
Git springt im Commit-Graph automatisch vor und zurück, um den fehlerhaften Commit schrittweise eingrenzen zu können.
Weitere Informationen: <https://git-scm.com/docs/git-bisect>.

- Starte eine Bisect-Session in einem Commit-Bereich, der durch einen bekannten fehlerhaften Commit und einen sauberen Commit begrenzt wird:

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fehlerhafter_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sauberer_commit</span>

- Prüfe jeden Commit, den `git bisect` auswählt, und kennzeichne ihn mit "gut" oder "schlecht":

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- Wechsle zum vorherigen Branch zurück, nachdem der fehlerhafte Commit lokalisiert wurde:

`git bisect reset`

- Überspringe einen Commit während der Bisect-Session (z.B. einen, der die Tests aufgrund eines anderen Problems nicht bestanden hat):

`git bisect skip`
