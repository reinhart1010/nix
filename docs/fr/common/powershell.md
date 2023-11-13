---
layout: page
title: common/powershell (français)
description: "Interface en ligne de commande et langage de script spécialement conçu pour l'administration système."
content_hash: 8d10fd65335745eb38d0548e37bfbcbd94462a63
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/powershell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/powershell.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/powershell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/powershell.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># powershell

Interface en ligne de commande et langage de script spécialement conçu pour l'administration système.
Plus d'informations : <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- Démarre une session Windows PowerShell dans une fenêtre d'invite de commande :

`powershell`

- Charge un fichier de console PowerShell spécifique :

`powershell -PSConsoleFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Démarre une session avec une version spécifiée de PowerShell :

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Empêche l’interface système de se fermer après avoir exécuté les commandes de démarrage :

`powershell -NoExit`

- Décrive le format des données envoyées à PowerShell :

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Texte|XML</span>

- Détermine comment la sortie de PowerShell est formatée :

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Texte|XML</span>

- Affiche l'aide :

`powershell -Help`
