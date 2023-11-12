---
layout: page
title: common/gh (français)
description: "Travailler harmonieusement avec GitHub depuis la ligne de commande."
content_hash: c3eb34c1448a290a018bfc62ebc7e1cded85dfb6
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/gh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gh.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh

Travailler harmonieusement avec GitHub depuis la ligne de commande.
Certaines commandes comme `gh config` ont leur propre documentation.
Plus d'informations : <https://cli.github.com/>.

- Clone un dépôt GitHub localement :

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépôt</span>

- Crée une nouvelle issue :

`gh issue create`

- Affiche et filtre les issues ouvertes du dépôt courant :

`gh issue list`

- Affiche une issue dans le navigateur Web par défaut :

`gh issue view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numéro_de_l'issue</span>

- Crée une pull request :

`gh pr create`

- Affiche une pull request dans le navigateur Web par défaut :

`gh pr view --web `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numéro_de_la_PR</span>

- Observe une pull request spécifique localement :

`gh pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numéro_de_la_PR</span>

- Affiche le statut des pull requests du dépôt courant:

`gh pr status`
