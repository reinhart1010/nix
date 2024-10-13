---
layout: page
title: common/autoconf (français)
description: "Génère des scripts de configuration pour configurer automatiquement les paquets du code source."
content_hash: 6bce52572a1f56375b23ad26c98766966a1ef8a4
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/autoconf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/autoconf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autoconf

Génère des scripts de configuration pour configurer automatiquement les paquets du code source.
Plus d'informations : <https://www.gnu.org/software/autoconf>.

- Génère un script de configuration depuis `configure.ac` (si présent) ou `configure.in` et le sauvegarde dans `configure` :

`autoconf`

- Génère un script de configuration depuis un modèle spécifié; et l'affiche la sortie standard :

`autoconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_template</span>

- Génère un script de configuration depuis un modèle spécifié (même si the fichier d'entrée n'a pas changé) et l'écrit dans un fichier :

`autoconf --force --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_sortie</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_template</span>
