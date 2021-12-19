---
layout: page
title: common/git-send-email (français)
description: "Envoyer une collection de correctifs par email."
content_hash: 384477a49ea815879e6d5585206586f99367a165
related_topics:
  - title: English version
    url: /en/common/git-send-email.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-send-email.html
    icon: bi bi-globe
---
# git send-email

Envoyer une collection de correctifs par email.
Les correctifs peuvent être spécifiés sous forme de fichiers, de directions ou de liste de révisions.
Plus d'informations : <https://git-scm.com/docs/git-send-email>.

- Envoyer le dernier commit de la branche courante :

`git send-email -1`

- envoyer un commit spécifique :

`git send-email -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- envoyer de multiples commits de la branche courante (ici : 10) :

`git send-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- Envoyez un e-mail de présentation de la série de correctifs :

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number of commits</span>` --compose`

- Consultez et modifiez l'e-mail de chaque patch que vous êtes sur le point d'envoyer :

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number of commits</span>` --annotate`
