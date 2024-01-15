---
layout: page
title: common/ssh-copy-id (français)
description: "Dépose une clé publique sur une machine distante, dans les clés autorisées `authorized_keys`."
content_hash: 18458dc0431b888052560dcb7d22c217b7ef0795
last_modified_at: 2024-01-15
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-copy-id.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-copy-id

Dépose une clé publique sur une machine distante, dans les clés autorisées `authorized_keys`.
Plus d'informations : <https://manned.org/ssh-copy-id>.

- Dépose toutes les clés publiques sur la machine distante :

`ssh-copy-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>

- Dépose une clé publique spécifique sur la machine distante :

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/certificat</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>

- Dépose une clé publique spécifique sur la machine distante en utilisant un port particulier :

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/certificat</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_utilisateur</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hote_distant</span>
