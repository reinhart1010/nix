---
layout: page
title: linux/certbot (Deutsch)
description: "The Let's Encrypt Agent zum automatischen Erhalten und Erneuern von TLS-Zertifikaten."
content_hash: 7bd5d91c9e4d4d08321baeb6417840b9a2cc6329
related_topics:
  - title: English version
    url: /en/linux/certbot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/certbot.html
    icon: bi bi-globe
---
# certbot

The Let's Encrypt Agent zum automatischen Erhalten und Erneuern von TLS-Zertifikaten.
Nachfolger von `letsencrypt`.
Weitere Informationen: <https://certbot.eff.org/docs/using.html>.

- Beziehe ein neues Zertifikat über die webroot-Autorisierung, aber ohne dieses automatisch zu installieren:

`sudo certbot certonly --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.beispiel.de</span>

- Beziehe ein neues Zertifikat über die nginx-Autorisierung und automatische Installation des neuen Zertifikats:

`sudo certbot --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.beispiel.de</span>

- Beziehe ein neues Zertifikat über die apache-Autorisierung und automatische Installation des neuen Zertifikats:

`sudo certbot --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.beispiel.de</span>

- Erneuere alle Let's Encrypt Zertifikate die in 30 Tagen oder weniger auslaufen (nicht vergessen alle Server, die diese nutzen, neu zu starten):

`sudo certbot renew`

- Simuliere die Zertifikatserneuerung, ohne diese zu speichern:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.beispiel.de</span>` --dry-run`

- Beziehe eine Test-Zertifikat:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.beispiel.de</span>` --test-cert`
