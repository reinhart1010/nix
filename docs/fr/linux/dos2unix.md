---
layout: page
title: linux/dos2unix (français)
description: "Remplace les fins de lignes de style DOS par des fins de lignes de style Unix."
content_hash: ca8bd8ff51ade10fcc45acda27cf9046fa443d99
last_modified_at: 2024-09-08
related_topics:
  - title: català version
    url: /ca/linux/dos2unix.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dos2unix.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dos2unix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dos2unix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dos2unix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dos2unix

Remplace les fins de lignes de style DOS par des fins de lignes de style Unix.
Remplace CRLF par LF.
Voir également `unix2dos`, `unix2mac`, et `mac2unix`.
Plus d'informations : <https://manned.org/dos2unix>.

- Remplace les fins de lignes d'un fichier :

`dos2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Crée une copie avec des fins de lignes de type Unix :

`dos2unix -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/nouveau_fichier</span>

- Affiche les informations d'un fichier :

`dos2unix -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Conserve/Ecrit/Supprime la marque d'ordre des octets (BOM) :

`dos2unix --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keep-bom|add-bom|remove-bom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
