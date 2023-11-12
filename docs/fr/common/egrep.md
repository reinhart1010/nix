---
layout: page
title: common/egrep (français)
description: "Recherche de motifs dans un texte. Supporte la version étendues des expressions regulieres (`?`, `+`, `{}`, `()`, et `|`)."
content_hash: ab4f39fbab98095c441bb95f6420055ec49909cd
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/egrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# egrep

Recherche de motifs dans un texte. Supporte la version étendues des expressions regulieres (`?`, `+`, `{}`, `()`, et `|`).
Plus d'informations : <https://manned.org/egrep>.

- Recherche une chaîne de caractères précise :

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Recherche une chaîne de caractères dans plusieurs fichiers :

`egrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier3</span>

- Utilise l'entrée standard au lieu d'un fichier :

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>` | egrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>

- Affiche le nom du fichier avec la ligne correspondante pour chaque concordance :

`egrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Recherche récursivement dans le dossier courant, en ignorant les fichiers binaires, une chaîne de caractères précise :

`egrep --recursive --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Inverse le résultat pour exclure des chaînes de caractères spécifiques :

`egrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chaîne_recherchée</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
