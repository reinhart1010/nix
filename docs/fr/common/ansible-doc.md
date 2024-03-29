---
layout: page
title: common/ansible-doc (français)
description: "Affiche les informations des modules installés dans les librairies Ansible."
content_hash: 25ad41f0e50ca012d681a314b91daec4bfb81934
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-doc.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-doc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-doc

Affiche les informations des modules installés dans les librairies Ansible.
Affiche une liste concise des plugins et leurs description courte.
Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-doc.html>.

- Liste les plugins action (modules) disponibles :

`ansible-doc --list`

- Liste les plugins disponible d'un certain type :

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_de_plugin</span>` --list`

- Affiche les informations sur un plugin action (module) spécifique :

`ansible-doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_plugin</span>

- Affiche les informations sur un plugin avec un certain type :

`ansible-doc --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_de_plugin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_plugin</span>

- Affiche le raccourci playbook d'un plugin action (module) :

`ansible-doc --snippet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_plugin</span>

- Affiche les informations sur un plugin action (module) en JSON :

`ansible-doc --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_plugin</span>
