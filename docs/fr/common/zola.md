---
layout: page
title: common/zola (français)
description: "Un générateur de site statique à partir d'un unique binaire sans dépendance."
content_hash: 364c27a39b32694b6a150fd7183b252356e56d42
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/zola.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zola.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zola

Un générateur de site statique à partir d'un unique binaire sans dépendance.
Plus d'informations : <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- Créer la structure du répertoire utilisé par Zola dans un répertoire donné :

`zola init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mon_site</span>

- Construit la totalité du site dans le répertoire `public` (si le répertoire existe, il est supprimé) :

`zola build`

- Construit la totalité du site dans un répertoire différent :

`zola build --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire_de_sortie/</span>

- Construit et met à disposition le site à partir d'un serveur local (l'adresse par défaut est `127.0.0.1:1111`) :

`zola serve`

- Construit l'ensemble des pages comme la commande `build`, sans écrire le résultat sur le disque :

`zola check`
