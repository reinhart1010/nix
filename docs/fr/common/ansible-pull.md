---
layout: page
title: common/ansible-pull (français)
description: "Récupère les playbook ansible depuis un dépôt VCS et exécute les en local."
content_hash: f6d2f3c4e8f11ec85d1a3e0f4626679b51af0095
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-pull

Récupère les playbook ansible depuis un dépôt VCS et exécute les en local.
Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-pull.html>.

- Récupère le playbook depuis un VCS et exécute le fichier par défaut local.yaml du playbook :

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_du_dépôt</span>

- Récupère le playbook depuis un VCS et exécute un playbook spécifique :

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_du_dépôt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Récupère un playbook depuis un VCS sur une branche spécifique et exécute ce dernier :

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_du_dépôt</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branche</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- Récupère un playbook depuis un VCS, spécifie les fichiers hôtes et exécute un playbook spécifique :

`ansible-pull -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_du_dépôt</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_hôtes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>
