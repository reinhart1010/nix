---
layout: page
title: common/arduino-builder (français)
description: "Un outil en ligne de commande pour compiler des croquis arduino."
content_hash: fcf5aa6a61396dcbcf661ce8d37c28827e8df66a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/arduino-builder.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino-builder.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arduino-builder

Un outil en ligne de commande pour compiler des croquis arduino.
AVERTISSEMENT DE DÉPRÉCIATION: Cet outil a été retiré au profit de `arduino`.
Plus d'informations : <https://github.com/arduino/arduino-builder>.

- Construis un croquis :

`arduino-builder -compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/croquis.ino</span>

- Spécifie the niveau de débogage (1 à 10, 5 par défaut) :

`arduino-builder -debug-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">niveau</span>

- Spécifie un dossier de construction :

`arduino-builder -build-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier/de/construction</span>

- Utilise un fichier d'option de construction, au lieu de spécifier `--hardware`, `--tools`, etc. Manuellement à chaque fois :

`arduino-builder -build-options-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/construction.options.json</span>

- Active le mode verbeux :

`arduino-builder -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
