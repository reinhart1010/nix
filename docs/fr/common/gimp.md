---
layout: page
title: common/gimp (français)
description: "Outil d'édition et de retouche d'image, libre et multiplateforme."
content_hash: 247cb3f23213158693ee6155de0b8530845d42c1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/gimp.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/gimp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gimp

Outil d'édition et de retouche d'image, libre et multiplateforme.
Voir aussi : `krita`.
Plus d'informations : <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

- Démarre GIMP :

`gimp`

- Démarre sans l'écran de démarrage :

`gimp --no-splash`

- Ouvre les fichiers spécifiés :

`gimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/image1 chemin/vers/image2 ...</span>

- Démarre une nouvelle instance, même si une instance est déjà en cours d'exécution :

`gimp --new-instance`

- Affiche les erreurs et les avertissements sur la console au lieu de les afficher dans une boîte de dialogue :

`gimp --console-messages`

- Active les routines de débogage des signaux non fatals :

`gimp --debug-handlers`
