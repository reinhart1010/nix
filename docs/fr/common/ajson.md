---
layout: page
title: common/ajson (français)
description: "Exécute un JSONPath sur un objet JSON."
content_hash: a50160dda09ef09bdad4f05cb60b5da6fef52cad
related_topics:
  - title: English version
    url: /en/common/ajson.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ajson

Exécute un JSONPath sur un objet JSON.
Plus d'informations : <https://github.com/spyzhov/ajson>.

- Lis un JSON depuis un fichier et exécute une expression JSONPath spécifique :

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.json</span>

- Lis un JSON depuis l'entrée standard et exécute une expression JSONPath spécifique :

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier.json</span>` | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`'`

- Lis un JSON depuis une URL et évalue une expression JSONPath spécifique :

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avg($..price)</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://exemple.com/api/</span>`'`

- Lis un JSON simple et calcule une valeur :

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`' | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2 * pi * $</span>`'`
