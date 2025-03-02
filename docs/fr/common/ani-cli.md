---
layout: page
title: common/ani-cli (français)
description: "Une CLI pour chercher et regarder des animés."
content_hash: 91b2033da501a5245df91c224fe991a21713d2bb
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ani-cli.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ani-cli.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ani-cli.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ani-cli.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ani-cli.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ani-cli.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/ani-cli.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ani-cli.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ani-cli.html
    icon: bi bi-globe
tldri18n_status: 1
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

`ani-cli -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numéro_de_l_épisode</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_l_animé</span>`"`

- Continue de regarder l'animé depuis l'historique :

`ani-cli -c`

- Met à jour `ani-cli` :

`ani-cli -U`
