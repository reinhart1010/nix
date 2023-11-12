---
layout: page
title: common/nano (français)
description: "Éditeur de texte simple et convivial. C'est un clone libre et amélioré de Pico."
content_hash: f7583a5092a852aeb56f64f137ef3faf5eb62772
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/nano.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nano.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nano.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nano.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nano

Éditeur de texte simple et convivial. C'est un clone libre et amélioré de Pico.
Plus d'informations : <https://nano-editor.org>.

- Ouvre un fichier :

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Ouvre un fichier en positionnant le curseur à une rangée et colonne donnée :

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ligne</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">colonne</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Active le défilement fluide :

`nano -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Indente les nouvelles lignes à la même indentation que les lignes précédentes :

`nano -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>

- Avant la modification, sauvegarde le fichier actuel sous le format `nom_du_fichier_actuel~` :

`nano -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier</span>
