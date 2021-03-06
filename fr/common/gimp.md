---
layout: page
title: common/gimp (français)
description: "Outil d'édition et de retouche d'image, libre et multiplateforme"
content_hash: a11f8cce7ebe33d35bafc9e01cc6e87a2e67754c
related_topics:
  - title: English version
    url: /en/common/gimp.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/gimp.html
    icon: bi bi-globe
---
# gimp

Outil d'édition et de retouche d'image, libre et multiplateforme
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
