---
layout: page
title: common/ani-cli (français)
description: "Une CLI pour chercher et regarder des animés."
content_hash: c9a9cac23af6d9c539417bbf71eeff3a11d82e22
related_topics:
  - title: Deutsch version
    url: /de/common/ani-cli.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ani-cli.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/ani-cli.html
    icon: bi bi-globe
---
# ani-cli

Une CLI pour chercher et regarder des animés.
Plus d'informations : <https://github.com/pystardust/ani-cli>.

- Cherche un anime par nom :

`ani-cli "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_animé</span>`"`

- Télécharge l'épisode :

`ani-cli -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_animé</span>`"`

- Utilise VLC comme lecteur de video :

`ani-cli -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_animé</span>`"`

- Spécifie un épisode à regarder :

`ani-cli -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numéro_de_l_épisode</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_animé</span>`"`

- Continue de regarder l'animé depuis l'historique :

`ani-cli -c`

- Met à jour `ani-cli` :

`ani-cli -U`
