---
layout: page
title: linux/apache2ctl (français)
description: "L'outil d'Interface en Lignes de Commandes (ILC) pour administrer le serveur web HTTP Apache."
content_hash: 6342864c1d9267bf9449ab3513f1a95cafb1abee
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/apache2ctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apache2ctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apache2ctl

L'outil d'Interface en Lignes de Commandes (ILC) pour administrer le serveur web HTTP Apache.
Cette commande est disponible sur une distribution Debian. Pour les distributions basées Red Hat, voir `httpd`.
Plus d'informations : <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- Démarre le démon Apache. Envoie un message s'il est déjà actif :

`sudo apache2ctl start`

- Arrête le démon Apache :

`sudo apache2ctl stop`

- Re-démarre le démon Apache :

`sudo apache2ctl restart`

- Teste la syntaxe du fichier de configuration :

`sudo apache2ctl -t`

- Liste les modules chargés :

`sudo apache2ctl -M`
