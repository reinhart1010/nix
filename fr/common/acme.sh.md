---
layout: page
title: common/acme.sh (français)
description: "Script shell implémentant le protocole client ACME, une alternative à certbot."
content_hash: 57988a9d2cadb6808663a8a8e5ac8114e8d427cb
related_topics:
  - title: English version
    url: /en/common/acme.sh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># acme.sh

Script shell implémentant le protocole client ACME, une alternative à certbot.
Voir aussi `acme.sh dns`.
Plus d'informations : <https://github.com/acmesh-official/acme.sh>.

- Publie un certificat en utilisant le mode webroot :

`acme.sh --issue --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>` --webroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/webroot</span>

- Publie un certificat pour plusieurs domaines en utilisant le mode autonome avec le port 80 :

`acme.sh --issue --standalone --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.exemple.com</span>

- Publie un certificat en utilisant le mode autonome TLS avec le port 443 :

`acme.sh --issue --alpn --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>

- Publie un certificat en utilisant une configuration Nginx :

`acme.sh --issue --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>

- Publie un certificat en utilisant une configuration Apache :

`acme.sh --issue --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>

- Publie un certificat wildcard (\*) en utilisant le mode automatique DNS API :

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.exemple.com</span>

- Installe les fichiers de certificat dans un dossier spécifique (Utile pour les renouvellements automatiques de certificat) :

`acme.sh --install-cert -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemple.com</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/exemple.com.key</span>` --fullchain-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/chemin/vers/exemple.com.cer</span>` --reloadcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"systemctl force-reload nginx"</span>
