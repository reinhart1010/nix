---
layout: page
title: common/ansible-inventory (français)
description: "Display or dump an Ansible inventory."
content_hash: 8aac85df8e2dcf35e55971047907610c54cad312
last_modified_at: 2024-01-15
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-inventory.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-inventory.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansible-inventory.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansible-inventory

Display or dump an Ansible inventory.
Voir aussi : `ansible`.
Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Affiche l'inventaire par défaut :

`ansible-inventory --list`

- Affiche un inventaire spécifique :

`ansible-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_script_ou_dossier</span>

- Affiche l'inventaire par défaut en YAML :

`ansible-inventory --list --yaml`

- Sauvegarde l'inventaire par défaut dans un fichier :

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
