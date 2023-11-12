---
layout: page
title: linux/eject (français)
description: "Éjecte les CD, disquettes et les bandes magnétiques."
content_hash: 08b10a6963964f4b94da1980682333cc01341a3c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/eject.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eject

Éjecte les CD, disquettes et les bandes magnétiques.
Plus d'informations : <https://manned.org/eject>.

- Affiche l'appareil par défaut :

`eject -d`

- Éjecte l'appareil par défaut :

`eject`

- Éjecte un appareil spécifique (l'ordre par défaut est CD-ROM, SCSI, Disquette puis bande magnétique) :

`eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- Bascule le support d'appareil en mode ouvert ou fermé :

`eject -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- Éjecte un CD :

`eject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- Éjecte une disquette :

`eject -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/disquette</span>

- Éjecte une bande magnétique :

`eject -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/bande</span>
