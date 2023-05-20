---
layout: page
title: common/astyle (italiano)
description: "Indentatore, formattatore e beautifier di codice sorgente per i linguaggi C, C++, C# e Java."
content_hash: 81e90931c6057d3b7ca236a0d17b1222449879dc
last_modified_at: 2023-05-20
related_topics:
  - title: English version
    url: /en/common/astyle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/astyle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/astyle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/astyle.html
    icon: bi bi-globe
---
# astyle

Indentatore, formattatore e beautifier di codice sorgente per i linguaggi C, C++, C# e Java.
Quando eseguito, una copia del file originale è creata con l'estensione ".orig" aggiunta come suffisso.
Maggiori informazioni: <http://astyle.sourceforge.net>.

- Applica lo stile di default di 4 spazi per livello di indentazione e nessun cambiamento alla formattazione:

`astyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_sorgente</span>

- Applica lo stile Java con parentesi graffe aperte sulla stessa riga (attached braces):

`astyle --style=java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Applica lo stile allman per parantesi graffe su linee separate (broken braces):

`astyle --style=allman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Applica un'indentazione personalizzata utilizzando spazi. Scegli tra 2 e 20 spazi:

`astyle --indent=spaces=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_spazi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Applica un'indentazione personalizzata utilizzando tab. Scegli tra 2 e 20 tab:

`astyle --indent=tab=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_tab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
