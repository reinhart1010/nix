---
layout: page
title: common/git-bisect (Deutsch)
description: "Benuzt binäre Suche um den commit ausfindig zu machen, welcher einen Fehler beinhaltet."
content_hash: f958d8cdce1bb0e328be21122c85e2e4474c0d8e
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
---
# git bisect

Benuzt binäre Suche um den commit ausfindig zu machen, welcher einen Fehler beinhaltet.
Git springt im Commit-Graph automatisch vor und zurück, um den fehlerhaften Commit schrittweise einzugrenzen zu können.
Weitere Informationen: <https://git-scm.com/docs/git-bisect>.

- Starte eine Bisect-Session in einem Commit-Bereich, der durch einen bekannten fehlerhaften Commit und einen sauberen Commit begrenzt wird:

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fehlerhafter_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sauberer_commit</span>

- Prüfe jeden Commit, den `git bisect` auswählt, und kennzeichne ihn mit "gut" oder "schlecht":

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- Wechsle zum vorherigen Branch zurück, nachdem der fehlerhafte Commit lokalisiert wurde:

`git bisect reset`

- Überspringe einen Commit während der Bisect-Session (z.B. einen, der die Tests aufgrund eines anderen Problems nicht bestanden hat):

`git bisect skip`
