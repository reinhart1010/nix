---
layout: page
title: common/fdupes (français)
description: "Trouve les fichiers dupliqués dans les dossiers donnés."
content_hash: b85f98a38aa9a57d6b53a89ceef75c0443e75e70
related_topics:
  - title: English version
    url: /en/common/fdupes.html
    icon: bi bi-globe
---
# fdupes

Trouve les fichiers dupliqués dans les dossiers donnés.
Plus d'informations : <https://github.com/adrianlopezroche/fdupes>.

- Chercher dans un dossier :

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier</span>

- Chercher dans plusieurs dossiers :

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier2</span>

- Chercher dans un dossier récursivement :

`fdupes -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier</span>

- Chercher dans plusieurs dossiers dont un récursivement :

`fdupes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier1</span>` -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier2</span>

- Chercher récursivement les dupliqués et demander les fichiers à conserver, supprimant les autres :

`fdupes -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier</span>

- Chercher récursivement et supprimer les dupliqués automatiquement :

`fdupes -rdN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dossier</span>
