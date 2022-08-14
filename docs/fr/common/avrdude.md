---
layout: page
title: common/avrdude (français)
description: "Pilotes pour programmer les microcontrôleurs Atmel AVR."
content_hash: 705de494016de3ddbb5df136594a3fb569daad48
related_topics:
  - title: Deutsch version
    url: /de/common/avrdude.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/avrdude.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/avrdude.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/avrdude.html
    icon: bi bi-globe
---
# avrdude

Pilotes pour programmer les microcontrôleurs Atmel AVR.
Plus d'informations : <https://www.nongnu.org/avrdude/>.

- Lire le contenu du microcontrôleur :

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appareil_AVR</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmeur</span>` -U flash:r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.hex</span>`:i`

- Écrire du contenu dans le microcontrôleur :

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">appareil_AVR</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmeur</span>` -U flash:w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.hex</span>

- Affiche les appareils AVR disponibles :

`avrdude -p \?`

- Affiche les programmeurs AVR disponibles :

`avrdude -c \?`
