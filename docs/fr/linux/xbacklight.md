---
layout: page
title: linux/xbacklight (français)
description: "Outil pour ajuster la luminosité du rétroéclairage en utilisant l'extension RandR."
content_hash: e2535312c359ded7f0822605f187e4b03e9f578f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/xbacklight.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbacklight

Outil pour ajuster la luminosité du rétroéclairage en utilisant l'extension RandR.
Plus d'informations : <https://gitlab.freedesktop.org/xorg/app/xbacklight>.

- Obtient le niveau de luminosité de l'écran actuel comme un pourcentage :

`xbacklight`

- Régle la luminosité de l'écran à 40% :

`xbacklight -set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>

- Augmente la luminosité de l'écran actuel de 25% :

`xbacklight -inc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- Diminue la luminosité de l'écran actuel de 75% :

`xbacklight -dec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">75</span>

- Augment la luminosité de l'écran à 100%, étendu sur 60 secondes (valeur donnée en ms), en 60 pas :

`xbacklight -set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` -time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60000</span>` -steps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>
