---
layout: page
title: common/asciidoctor (français)
description: "Un processeur qui convertit des fichiers AsciiDoc vers un format publiable."
content_hash: b16485047335f96837e4371878a2397d2ceac685
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># asciidoctor

Un processeur qui convertit des fichiers AsciiDoc vers un format publiable.
Plus d'informations : <https://docs.asciidoctor.org>.

- Convertis un fichier `.adoc` vers un fichier HTML (le format de sortie par défaut) :

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>

- Convertis un fichier `.adoc` vers un fichier HTML et lie une feuille de style CSS :

`asciidoctor -a stylesheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/feuille_de_style.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>

- Convertis un fichier `.adoc` vers un fichier HTML embarqué, en enlevant tout sauf le body :

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>

- Convertis un fichier `.adoc` vers un PDF en utilisant la librairie `asciidoctor-pdf` :

`asciidoctor --backend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.adoc</span>
