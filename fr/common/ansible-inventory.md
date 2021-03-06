---
layout: page
title: common/ansible-inventory (français)
description: "Display or dump an Ansible inventory."
content_hash: 4b651b2f22178a25339c62048bf0aa91d344c745
related_topics:
  - title: English version
    url: /en/common/ansible-inventory.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-inventory

Display or dump an Ansible inventory.
Voir aussi : `ansible`.
Plus d'informations : <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- Affiche l'inventaire par défaut :

`ansible-inventory --list`

- Affiche un inventaire spécifique :

`ansbile-inventory --list --inventory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier_ou_script_ou_dossier</span>

- Affiche l'inventaire par défaut en YAML :

`ansible-inventory --list --yaml`

- Sauvegarde l'inventaire par défaut dans un fichier :

`ansible-inventory --list --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
