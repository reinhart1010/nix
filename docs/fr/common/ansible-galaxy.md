---
layout: page
title: common/ansible-galaxy (français)
description: "Crée et gère les rôles Ansible."
content_hash: b977f9bf810fa47d45584299552cf481bb72f6f2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansible-galaxy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-galaxy

Crée et gère les rôles Ansible.
Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- Installe un rôle :

`ansible-galaxy install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_rôle</span>

- Enlève un rôle :

`ansible-galaxy remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_rôle</span>

- Liste les rôles installés :

`ansible-galaxy list`

- Recherche pour un role donné :

`ansible-galaxy search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_rôle</span>

- Crée un nouveau rôle :

`ansible-galaxy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_rôle</span>

- Récupère les informations sur le rôle d'un utilisateur :

`ansible-galaxy role info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_rôle</span>

- Récupère les informations d'une collection :

`ansible-galaxy collection info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_d_utilisateur</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_la_collection</span>
