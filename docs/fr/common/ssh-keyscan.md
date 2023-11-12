---
layout: page
title: common/ssh-keyscan (français)
description: "Récupère les clés SSH publiques de machines distantes."
content_hash: 7a0e7eee675a1fed20d40ad4647048d3c3e6950b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-keyscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-keyscan

Récupère les clés SSH publiques de machines distantes.
Plus d'informations : <https://man.openbsd.org/ssh-keyscan>.

- Récupère toutes les clés d'une machine distante :

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>

- Récupère toutes les clés d'une machine distante en écoutant sur un port particulier :

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>

- Récupère un type particulier de clés d'une machine distante :

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>

- Met à jour manuellement le fichier `known_hosts` des hôtes connus avec l'empreinte d'une :

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>` >> ~/.ssh/known_hosts`
