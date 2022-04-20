---
layout: page
title: windows/powershell (français)
description: "Interface en ligne de commande et langage de script spécialement conçu pour l'administration système."
content_hash: fe658995869e2278c7d29ca4be25cc1aa357238c
related_topics:
  - title: English version
    url: /en/windows/powershell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/powershell.html
    icon: bi bi-globe
---
# powershell

Interface en ligne de commande et langage de script spécialement conçu pour l'administration système.
Plus d'informations : <https://docs.microsoft.com/windows-server/administration/windows-commands/powershell>.

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
