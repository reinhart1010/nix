---
layout: page
title: common/shards (français)
description: "Outil de gestion des dépendances pour le langage Crystal."
content_hash: db83ff2061cc7e388ffcea4fbe09f211bb0758ff
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/shards.html
    icon: bi bi-globe
---
# shards

Outil de gestion des dépendances pour le langage Crystal.
Plus d'informations : <https://crystal-lang.org/reference/the_shards_command>.

- Créé un fichier `shard.yml` squelette :

`shards init`

- Installe les dépendances à partir d'un fichier `shard.yml` :

`shards install`

- Met à jour toutes les dépendances :

`shards update`

- Liste toutes les dépendances installées :

`shards list`

- Liste la version d'une dépendance ayant un chemin donné :

`shards version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dependency_directory</span>
