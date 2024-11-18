---
layout: page
title: windows/add-appxpackage (français)
description: "Un utilitaire PowerShell pour ajouter un paquet d'applications signé (`.appx`, `.msix`, `.appxbundle`, `.appxbundle` et `.msixbundle`) à un compte utilisateur."
content_hash: 046f5e7661c7cb1043ef16461f032cf873fe3823
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/windows/add-appxpackage.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/add-appxpackage.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/add-appxpackage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Add-AppxPackage

Un utilitaire PowerShell pour ajouter un paquet d'applications signé (`.appx`, `.msix`, `.appxbundle`, `.appxbundle` et `.msixbundle`) à un compte utilisateur.
Plus d'informations : <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- Ajoute un paquet d'application :

`Add-AppxPackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin\vers\paquet.msix</span>

- Ajoute un paquet d'application avec ses dependences :

`Add-AppxPackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin\vers\paquet.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin\vers\dependences.msix</span>

- Installe une application en utilisant le fichier d'installation de l'application :

`Add-AppxPackage -AppInstallerFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin\vers\application.appinstaller</span>

- Ajoute un paquet non signé :

`Add-AppxPackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin\vers\paquet.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin\vers\dependences.msix</span>` -AllowUnsigned`
