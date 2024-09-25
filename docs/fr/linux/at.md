---
layout: page
title: linux/at (français)
description: "Exécute des commandes à des temps détermintés."
content_hash: 028d7e5b56d2b4c08c7cb80a07b6e3ee986bb9a0
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/at.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Exécute des commandes à des temps détermintés.
Plus d'informations : <https://manned.org/at.1>.

- Ouvre une invite `at` afin de créer un nouvel ensemble de commandes programmées, presser `Ctrl + D` pour sauvegarder et quitter :

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Exécute les commandes et envoie les résultats par mail en utilisant un programme de messagerie local comme Sendmail :

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -m`

- Exécute un script à un temps donné :

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script</span>

- Affiche une notification système à 23 heures le 18 Février :

`echo "notify-send '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Debout !</span>`'" | at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11pm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Feb 18</span>
