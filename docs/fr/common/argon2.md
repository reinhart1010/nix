---
layout: page
title: common/argon2 (français)
description: "Calcule les hachés cryptographiques d'Argon2."
content_hash: 788a1926233fb40eedf223f289f377033c105226
last_modified_at: 2024-11-23
related_topics:
  - title: English version
    url: /en/common/argon2.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/argon2.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/argon2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argon2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# argon2

Calcule les hachés cryptographiques d'Argon2.
Plus d'informations : <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Calcule un haché avec un mot de passe et un sel avec les paramètres par défaut :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sel</span>`"`

- Calcule un haché avec l'algorithme spécifié :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sel</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|i|id</span>

- Affiche le haché de sortie sans informations supplémentaires :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sel</span>`" -e`

- Calcule un haché avec des [t]emps d'itération, l'utilisation de la [m]émoire et des paramètres de [p]arallélisme donnés :

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mot_de_passe</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sel</span>`" -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
