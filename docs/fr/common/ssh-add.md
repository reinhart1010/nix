---
layout: page
title: common/ssh-add (français)
description: "Gère les clés SSH enregistrées dans l'agent SSH `ssh-agent`."
content_hash: c592bbcf05569c3d05ff73b33beee0359c88e385
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ssh-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-add.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ssh-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-add

Gère les clés SSH enregistrées dans l'agent SSH `ssh-agent`.
S'assurer que `ssh-agent` est en fonctionnement pour enregistrer des clés.
Plus d'informations : <https://man.openbsd.org/ssh-add>.

- Ajoute les clés présentes dans `~/.ssh` (clés par défaut) à l'agent SSH :

`ssh-add`

- Ajoute une clé spécifique à l'agent SSH :

`ssh-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>

- Liste les empreintes des clés actuellement enregistrées :

`ssh-add -l`

- Supprime une clé de l'agent SSH :

`ssh-add -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>

- Supprime toutes les clés enregistrées de l'agent SSH :

`ssh-add -D`

- Ajoute une clé spécifique à l'agent SSH et au trousseau de clés :

`ssh-add -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/clé_privée</span>
