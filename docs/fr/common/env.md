---
layout: page
title: common/env (français)
description: "Affiche l'environnement ou exécute un programme dans un environnement modifié."
content_hash: 2bdd5aaef4214a7c4978f777dc930772f974eb97
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/env.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/env.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/env.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/env.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/env.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# env

Affiche l'environnement ou exécute un programme dans un environnement modifié.
Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Affiche l'environnement :

`env`

- Exécute le programme donné. Souvent utilisé dans les scripts après le shebang (`#!`) pour consulter le chemin vers le programme :

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programme</span>

- Exécute le programme donné, avec un environnement vide :

`env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programme</span>

- Supprime une variable d'environnement et execute le programme donné :

`env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programme</span>

- Définit ou modifie une variable d'environnement et execute le programme donné :

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programme</span>

- Définit ou modifie plusieurs variables d'environnement et execute le programme donné :

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable3</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valeur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programme</span>
