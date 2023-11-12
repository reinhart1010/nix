---
layout: page
title: common/adguardhome (français)
description: "Un logiciel réseau pour bloquer les pubs et les traqueurs."
content_hash: 3aaeaa9142f969b3fb3c79ba06aefe4ffe0f22b2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/adguardhome.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adguardhome.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adguardhome.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adguardhome.html
    icon: bi bi-globe
tldri18n_status: 2
---
# AdGuardHome

Un logiciel réseau pour bloquer les pubs et les traqueurs.
Plus d'informations : <https://github.com/AdguardTeam/AdGuardHome>.

- Lance AdGuard Home :

`AdGuardHome`

- Lance AdGuard Home avec une configuration spécifique :

`AdGuardHome --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/AdGuardHome.yaml</span>

- Configure le répertoire de travail où les données seront stockées :

`AdGuardHome --work-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/répertoire</span>

- Installe ou désinstalle AdGuard Home comme un service :

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>

- Démarre le service AdGuard Home :

`AdGuardHome --service start`

- Recharge la configuration pour le service AdGuard Home :

`AdGuardHome --service reload`

- Éteint ou redémarre le service AdGuard Home :

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stop|restart</span>
