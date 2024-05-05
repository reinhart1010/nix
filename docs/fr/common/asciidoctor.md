---
layout: page
title: common/asciidoctor (français)
description: "Un processeur qui convertit des fichiers AsciiDoc vers un format publiable."
content_hash: b2a63c2d3e03ee3552ec38230dcf3c179af37411
last_modified_at: 2024-05-05
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciidoctor.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/asciidoctor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciidoctor

Un processeur qui convertit des fichiers AsciiDoc vers un format publiable.
Plus d'informations : <https://docs.asciidoctor.org>.

- Convertis un fichier `.adoc` vers un fichier HTML (le format de sortie par défaut) :

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>

- Convertis un fichier `.adoc` vers un fichier HTML et lie une feuille de style CSS :

`asciidoctor -a stylesheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/feuille_de_style.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>

- Convertis un fichier `.adoc` vers un fichier HTML embarqué, en enlevant tout sauf le body :

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>

- Convertis un fichier `.adoc` vers un PDF en utilisant la librairie `asciidoctor-pdf` :

`asciidoctor --backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>
