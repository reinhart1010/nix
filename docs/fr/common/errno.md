---
layout: page
title: common/errno (français)
description: "Recherche les noms et descriptions des codes errno."
content_hash: 344be6a7c133b63fe96ca5317648f5618c1fdf16
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/errno.html
    icon: bi bi-globe
tldri18n_status: 2
---
# errno

Recherche les noms et descriptions des codes errno.
Plus d'informations : <https://joeyh.name/code/moreutils/>.

- Recherche la description d'une erreur par nom ou par code :

`errno `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom|code</span>

- Liste tous les noms, codes et descriptions d'errno :

`errno --list`

- Cherche les codes dont la description contient le texte entier indiqué :

`errno --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texte</span>

- Cherche les codes dont la description contient le texte entier indiqué (dans toutes les langues) :

`errno --search-all-locales `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texte</span>
