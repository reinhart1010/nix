---
layout: page
title: common/ansible-vault (français)
description: "Chiffre & déchiffre des valeurs, des structures de données et des fichiers dans un projet Ansible."
content_hash: 4e1ef795cda491f8ce0ba507ae7f267dbdacbf58
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-vault.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-vault.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-vault

Chiffre & déchiffre des valeurs, des structures de données et des fichiers dans un projet Ansible.
Plus d'informations : <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Crée un nouveau fichier vault chiffré avec une invite à rentrer un mot passe :

`ansible-vault create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_vault</span>

- Crée un nouveau fichier vault chiffré avec un fichier clé vault pour le chiffrer :

`ansible-vault create --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_mot_de_passe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_vault</span>

- Chiffre un ficher existant avec un fichier de mot de passe optionnel :

`ansible-vault encrypt --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_mot_de_passe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_vault</span>

- Chiffre un texte avec le format de chiffrage pour textes d'Ansible, en affichant une invite interactif :

`ansible-vault encrypt_string`

- Affiche un fichier chiffré, en utilisant un fichier de mot de passe pour le déchiffrer :

`ansible-vault view --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_de_mot_de_passe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_vault</span>

- Remplace le fichier de mot de passe d'un fichier vault déjà chiffré par un autre :

`ansible-vault rekey --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_fichier_de_mot_de_passe</span>` --new-vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouveau_fichier_de_mot_de_passe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fichier_vault</span>
