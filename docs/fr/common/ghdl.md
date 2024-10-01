---
layout: page
title: common/ghdl (français)
description: "Simulateur à source ouvert pour le langage VHDL."
content_hash: 58c236753413e2946343b87faeb60b603c6ae2a6
last_modified_at: 2024-10-01
related_topics:
  - title: English version
    url: /en/common/ghdl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghdl

Simulateur à source ouvert pour le langage VHDL.
Plus d'informations : <https://ghdl.github.io/ghdl/>.

- Analyse un fichier de source VHDL et génère un fichier objet :

`ghdl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.vhdl</span>

- Élabore un design (où `design` est le nom d'une unité de configuration, d'entité, ou d'architecture) :

`ghdl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Exécute un design élaboré :

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Exécute un design élaboré et sauvegarde la sortie à un fichier de forme d'onde :

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>` --wave=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sortie.ghw</span>

- Vérifie le syntaxe d'un fichier de source VHDL :

`ghdl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.vhdl</span>

- Affiche l'aide générale :

`ghdl --help`
