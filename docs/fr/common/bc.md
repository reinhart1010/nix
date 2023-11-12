---
layout: page
title: common/bc (français)
description: "Un langage de calcul de précision arbitraire."
content_hash: ec292e079d9c23aced53f8b275b55c6fe7b86da3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

Un langage de calcul de précision arbitraire.
Voir aussi : `dc`.
Plus d'informations : <https://manned.org/man/bc.1>.

- Démarre une session interactive :

`bc`

- Démarre une session interactive avec la bibliothèque mathématique standard activée :

`bc --mathlib`

- Calcule une expression :

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Exécute un script :

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/script.bc</span>

- Calcule une expression avec l'échelle spécifiée :

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- Calcule une fonction sinus/cosinus/arctangente/logarithme naturel/exponentielle en utilisant `mathlib` :

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)' | bc --mathlib`
