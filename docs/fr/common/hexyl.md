---
layout: page
title: common/hexyl (français)
description: "Un simple visualiseur hexadécimal pour le terminal. Il utilise des couleurs pour distinguer les différentes catégories d'octets."
content_hash: c61c1bd17aed7488c01b73bc82db3debb3d5f1cf
last_modified_at: 2024-02-23
related_topics:
  - title: English version
    url: /en/common/hexyl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexyl

Un simple visualiseur hexadécimal pour le terminal. Il utilise des couleurs pour distinguer les différentes catégories d'octets.
Plus d'informations : <https://github.com/sharkdp/hexyl>.

- Affiche la représentation hexadécimale d'un fichier :

`hexyl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche la représentation hexadécimale des n premiers octets d'un fichier :

`hexyl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche les octets 512 à 1024 d'un fichier :

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>

- Affiche 512 octets en commençant par le 1024e octet :

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>`:+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier</span>
