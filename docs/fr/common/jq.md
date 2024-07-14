---
layout: page
title: common/jq (français)
description: "Un processeur JSON en ligne de commande qui utilise un langage dédié (DSL)."
content_hash: a60cda26bce08a2f2a20d50f43dafadd1cb99230
last_modified_at: 2024-07-14
related_topics:
  - title: Deutsch version
    url: /de/common/jq.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/jq.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/jq.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># jq

Un processeur JSON en ligne de commande qui utilise un langage dédié (DSL).
Plus d'informations : <https://jqlang.github.io/jq/manual/>.

- Exécute une expression spécifique (affiche une sortie JSON coloré et formaté) :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat chemin/vers/fichier.json</span>` | jq '.'`

- Exécute un script spécifique :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat chemin/vers/fichier.json</span>` | jq --from-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/script.jq</span>

- Transmet des arguments spécifiques :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat chemin/vers/fichier.json</span>` | jq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--arg "nom1" "valeur1" --arg "nom2" "valeur2" ...</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">. + $ARGS.named</span>`'`

- Imprime des clés spécifiques :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat chemin/vers/fichier.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.clé1, .clé2, ...</span>`'`

- Imprime des éléments spécifiques du tableau :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat chemin/vers/fichier.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.[index1], .[index2], ...</span>`'`

- Imprime tous les éléments du tableau/les clés de l'objet :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat chemin/vers/fichier.json</span>` | jq '.[]'`

- Ajoute/supprime des clés spécifiques :

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat chemin/vers/fichier.json</span>` | jq '. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"clé1": "valeur1", "clé2": "valeur2", ...}</span>`'`
