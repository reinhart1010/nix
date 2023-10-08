---
layout: page
title: common/bun (français)
description: "Moteur d'exécution et boîte à outils JavaScript."
content_hash: b8a157ec2c4e8ed34d90ce1c84cf1a51954685bc
last_modified_at: 2023-10-08
related_topics:
  - title: English version
    url: /en/common/bun.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bun

Moteur d'exécution et boîte à outils JavaScript.
Comprend un empaqueteur, un exécuteur de tests et un gestionnaire de paquets.
Plus d'informations : <https://bun.sh>.

- Exécute un fichier JavaScript ou un script référencé dans `package.json` :

`bun run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier|nom_script</span>

- Exécute les tests unitaires :

`bun test`

- Télécharge et installe tous les paquets listés comme dépendances dans `package.json` :

`bun install`

- Ajoute une dépendance à `package.json` :

`bun add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_module</span>

- Supprime une dépendance de `package.json` :

`bun remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_module</span>

- Crée un nouveau projet Bun dans le répertoire actuel :

`bun init`

- Démarre un REPL (shell interactif) :

`bun repl`

- Met à jour Bun vers la dernière version :

`bun upgrade`
