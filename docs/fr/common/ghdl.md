---
layout: page
title: common/ghdl (français)
description: "Simulateur à source ouvert pour le langage VHDL."
content_hash: f337b081e9a6293a8e76dec4048cf3a3922ea7ed
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ghdl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghdl

Simulateur à source ouvert pour le langage VHDL.
Plus d'informations : <http://ghdl.free.fr>.

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
