---
layout: page
title: common/cmake (français)
description: "Système de construction logicielle multiplateforme, qui permet de générer des recettes de construction pour les systèmes de construction natifs."
content_hash: 2f2118acf0432a6b2dba2c4ec5752cfb31b19d7a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cmake.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cmake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmake.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cmake.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmake

Système de construction logicielle multiplateforme, qui permet de générer des recettes de construction pour les systèmes de construction natifs.
Plus d'informations : <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Génère une recette de construction `CMakeLists.txt` depuis le répertoire d'un projet :

`cmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire_du_projet</span>

- Génère une recette de construction, en définissant le type de construction à `Release` à l'aide d'une variable CMake :

`cmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire_du_projet</span>` -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CMAKE_BUILD_TYPE=Release</span>

- Utilise une recette déjà générée dans un répertoire donné pour construire les artefacts :

`cmake --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire_de_construction</span>

- Installe les artefacts de construction dans `/usr/local/` et retirer les symboles de débogage :

`cmake --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire_de_construction</span>` --strip`

- Installe les artefacts de construction en utilisant un préfixe personnalisé pour les chemins :

`cmake --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire_de_construction</span>` --strip --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire</span>

- Lance une cible de construction personnalisée :

`cmake --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire_de_construction</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_cible</span>
