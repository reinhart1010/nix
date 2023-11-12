---
layout: page
title: common/git-send-email (français)
description: "Envoyer une collection de correctifs par email."
content_hash: af3c11afdba044e41f47e87e354aa35a93e63eee
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-send-email.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-send-email.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-send-email.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git send-email

Envoyer une collection de correctifs par email.
Les correctifs peuvent être spécifiés sous forme de fichiers, de directions ou de liste de révisions.
Plus d'informations : <https://git-scm.com/docs/git-send-email>.

- Envoyer le dernier commit de la branche courante :

`git send-email -1`

- Envoyer un commit spécifique :

`git send-email -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Envoyer de multiples commits de la branche courante (ici : 10) :

`git send-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- Envoyez un e-mail de présentation de la série de correctifs :

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number of commits</span>` --compose`

- Consultez et modifiez l'e-mail de chaque patch que vous êtes sur le point d'envoyer :

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number of commits</span>` --annotate`
