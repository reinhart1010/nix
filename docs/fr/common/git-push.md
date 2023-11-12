---
layout: page
title: common/git-push (français)
description: "Pousse les commits vers un dépôt distant."
content_hash: c4b91775f50754e25ea3a2e33bb056f6471c8cce
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-push.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git push

Pousse les commits vers un dépôt distant.
Plus d'informations : <https://git-scm.com/docs/git-push>.

- Envoie les changements locaux dans la branche courante vers sa contrepartie distante :

`git push`

- Envoie les changements locaux d'une branche spécifique vers sa contrepartie distante :

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_branch</span>

- Publie la branche courante vers un dépôt distant, crée le nom de la branche distante :

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_distante</span>

- Envoi les changements locaux sur toutes les branches locales vers leur contrepartie sur le dépôt distant :

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>

- Supprime une branche dans un dépôt distant :

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche_distante</span>

- Supprime les branches distantes qui n'ont pas de contrepartie locale :

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_distant</span>

- Publie les tags qui ne sont pas sur le dépôt distant :

`git push --tags`
