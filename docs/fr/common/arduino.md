---
layout: page
title: common/arduino (français)
description: "Arduino Studio - Environnement de Développement Intégré pour la plateforme Arduino."
content_hash: d8c84f99a03ad950a1dfe377b6430165168551a0
related_topics:
  - title: English version
    url: /en/common/arduino.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino.html
    icon: bi bi-globe
---
# arduino

Arduino Studio - Environnement de Développement Intégré pour la plateforme Arduino.
Plus d'informations : <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Construis un croquis :

`arduino --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/croquis.ino</span>

- Construis et téléverse un croquis :

`arduino --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/croquis.ino</span>

- Construis et téléverse un croquis vers un Arduino Nano avec un CPU Atmega328p, connecté sur le port `/dev/ttyACM0` :

`arduino --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arduino:avr:nano:cpu=atmega328p</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyACM0</span>` --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/croquis.ino</span>

- Configure la préférence `nom` à une valeur `valeur` :

`arduino --pref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur</span>

- Construis un croquis, mets le résultat de ce dernier dans un dossier, et réutilise n'importe quelles versions précédentes dans ce dossier :

`arduino --pref build.path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier/de/construction</span>` --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/croquis.ino</span>

- Sauvegarde toutes préférences (modifiées) dans un fichier `preferences.txt` :

`arduino --save-prefs`
