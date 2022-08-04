---
layout: page
title: common/ghdl (français)
description: "Simulateur à source ouvert pour le langage VHDL."
content_hash: 1b4bbe1171e30731642a7325c18ac6d1f060796e
related_topics:
  - title: English version
    url: /en/common/ghdl.html
    icon: bi bi-globe
---
# ghdl

Simulateur à source ouvert pour le langage VHDL.
Plus d'informations : <http://ghdl.free.fr>.

- Analyse un fichier de source VHDL et génère un fichier objet :

`ghdl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.vhdl</span>

- Élabore un design (où <span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span> est le nom d'une unité de configuration, d'entité, ou d'architecture) :

`ghdl -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Exécute un design élaboré :

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>

- Exécute un design élaboré et sauvegarde la sortie à un fichier de forme d'onde :

`ghdl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">design</span>` --wave=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sortie.ghw</span>

- Vérifie le syntaxe d'un fichier de source VHDL :

`ghdl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier.vhdl</span>

- Affiche l'aide générale :

`ghdl --help`
