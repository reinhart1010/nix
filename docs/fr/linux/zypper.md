---
layout: page
title: linux/zypper (français)
description: "SUSE & openSUSE utilitaire de gestion de paquets."
content_hash: d72d8ac82be76c4299a0ca7d58c71cee23e2e4c0
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/zypper.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zypper

SUSE & openSUSE utilitaire de gestion de paquets.
Plus d'informations : <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchroniser la liste des paquets et versions disponibles :

`zypper refresh`

- Installer un nouveau paquet :

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Supprimer un paquet :

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Mettre à jour un paquet installé vers la version la plus récente disponible :

`zypper update`

- Chercher un paquet par mot clef :

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_clef</span>

- Afficher les informations concernant les dépôts de paquets configurés :

`zypper repos --sort-by-priority`
