---
layout: page
title: common/git-bisect (français)
description: "Utiliser une recherche binaire pour trouver le commit qui a introduit un bug."
content_hash: 828fef7ea8031bc05fc9a6e58504d77af3e904a9
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git bisect

Utiliser une recherche binaire pour trouver le commit qui a introduit un bug.
Git saute automatiquement d'avant en arrière dans le graphe de commit pour isoler le commit défectueux.
Plus d'informations : <https://git-scm.com/docs/git-bisect>.

- Démarrez une dissection sur une plage de commit délimitée par un bug connu et un commit propre connu (généralement plus ancien) :

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bad_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good_commit</span>

- Pour chaque `git bisect` sélectionné, le marquer comme "mauvais" (`bad`) ou "bon" (`good`) après l'avoir testé pour le problème :

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- Après que `git bisect` pointe vers le mauvais commit, terminer la dissection et retourner à la branche précédente :

`git bisect reset`

- Sauter un commit lors de la dissection (e.g. celui qui échoue les tests pour une autre raison) :

`git bisect skip`
