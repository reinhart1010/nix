---
layout: page
title: common/ani-cli (français)
description: "Une CLI pour chercher et regarder des animés."
content_hash: 98a83d5c11210f2b1d048ac10eb2d702e3106ed9
related_topics:
  - title: English version
    url: /en/common/ani-cli.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ani-cli

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

- Met à jour ani-cli :

`ani-cli -U`
