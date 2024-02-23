---
layout: page
title: common/mktemp (français)
description: "Crée un fichier ou un répertoire temporaire."
content_hash: e35f2d72a6516ae11c47f7b35330c53ad3a9b34a
last_modified_at: 2024-02-23
related_topics:
  - title: English version
    url: /en/common/mktemp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mktemp

Crée un fichier ou un répertoire temporaire.
Plus d'informations : <https://man.openbsd.org/mktemp.1>.

- Crée un fichier temporaire vide et affiche son chemin d'accès absolu :

`mktemp`

- Utilise un répertoire personnalisé si `$TMPDIR` n'est pas défini (la valeur par défaut dépend de la plateforme, mais est habituellement `/tmp`) :

`mktemp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/reptemp</span>

- Utilise un modèle de chemin personnalisé (les `X` sont remplacés par des caractères alphanumériques aléatoires) :

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/exemple.XXXXXXXX</span>

- Utilise un modèle de nom de fichier personnalisé :

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.XXXXXXXX</span>

- Crée un répertoire temporaire vide et affiche son chemin d'accès absolu :

`mktemp -d`
