---
layout: page
title: common/gimp (français)
description: "Outil d'édition et de retouche d'image, libre et multiplateforme."
content_hash: d430e8b4906d7c26ba1fe571ec54a2c0aed2a77c
last_modified_at: 2023-12-28
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

- Ouvre les fichiers spécifiés :

`gimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/image1 chemin/vers/image2 ...</span>

- Ouvre les fichiers spécifiés avec une nouvelle Démarre une nouvelle cadre :

`gimp --new-instance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/image1 chemin/vers/image2 ...</span>

- Démarre sans l'écran de démarrage :

`gimp --no-splash`

- Affiche les erreurs et les avertissements sur la console au lieu de les afficher dans une boîte de dialogue :

`gimp --console-messages`

- Active les routines de débogage des signaux non fatals :

`gimp --debug-handlers`
