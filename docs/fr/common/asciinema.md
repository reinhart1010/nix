---
layout: page
title: common/asciinema (français)
description: "Enregistre et rejoue les sessions de terminal, et également partageable sur asciinema.org."
content_hash: 900ff6061e9e75e906eff8f6fc0c4f46a6a41297
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asciinema.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciinema

Enregistre et rejoue les sessions de terminal, et également partageable sur asciinema.org.
Plus d'informations : <https://asciinema.org/docs/usage>.

- Associe l’installation locale de `asciinema` avec un compte asciinema.org :

`asciinema auth`

- Crée un nouvel enregistrement (une fois fini, l'utilisateur sera questionné pour l'enregistrer localement ou l'envoyer en ligne) :

`asciinema rec`

- Crée un nouvel enregistrement et l'enregistre dans un fichier local :

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>`.cast`

- Rejoue un enregistrement depuis un fichier local :

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>`.cast`

- Rejoue un enregistrement depuis asciinema.org :

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_d_enregistrement</span>

- Crée un nouvel enregistrement, en limitant le temps d’inactivité au maximum à 2.5 secondes :

`asciinema rec -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.5</span>

- Affiche la sortie complète d'un enregistrement local :

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>`.cast`

- Envoie un enregistrement local vers asciinema.org :

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>`.cast`
