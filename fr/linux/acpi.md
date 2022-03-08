---
layout: page
title: linux/acpi (français)
description: "Affiche l'état de la batterie ou des renseignements sur la température."
content_hash: 761a7905dbf31d59a54c39067844225974207a9f
related_topics:
  - title: català version
    url: /ca/linux/acpi.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/acpi.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/acpi.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/acpi.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/acpi.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># acpi

Affiche l'état de la batterie ou des renseignements sur la température.
Plus d'informations : <https://sourceforge.net/projects/acpiclient/files/acpiclient/>.

- Affiche les informations sur la batterie :

`acpi`

- Affiche les informations sur la température :

`acpi -t`

- Afficher les informations sur le dispositif de refroidissement :

`acpi -c`

- Afficher les informations sur le dispositif de refroidissement en Fahrenheit :

`acpi -tf`

- Afficher toutes les informations :

`acpi -V`

- Extraye les informations depuis `/proc` au lieu de `/sys` :

`acpi -p`
