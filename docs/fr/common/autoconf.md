---
layout: page
title: common/autoconf (français)
description: "Génère des scripts de configuration pour configurer automatiquement les paquets du code source."
content_hash: ed80e2b4ea80953f6db4242e2c5bd01d979088bb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/autoconf.html
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

`autoconf --force --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_sortie</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_template</span>
