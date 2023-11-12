---
layout: page
title: linux/certbot (Nederlands)
description: "De Let's Encrypt Agent om automatisch TLS certificaten te verkrijgen en te vernieuwen."
content_hash: c1d278191a9cdd68b06c009b75f4c5d0dd78acfd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/certbot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/certbot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/certbot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certbot

De Let's Encrypt Agent om automatisch TLS certificaten te verkrijgen en te vernieuwen.
Opvolger van `letsencrypt`.
Meer informatie: <https://certbot.eff.org/docs/using.html>.

- Verkrijg een nieuw certificaat via webroot authorisatie, maar installeer het certificaat niet automatisch:

`sudo certbot certonly --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomein.voorbeeld.com</span>

- Verkrijg een nieuw certificaat via nginx authorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomein.voorbeeld.com</span>

- Verkrijg een nieuw certificaat via apache authorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomein.voorbeeld.com</span>

- Vernieuw alle Let's Encrypt certificaten die binnen 30 dagen verlopen (vergeet achteraf niet alle servers te herstarten die dit certificaat gebruiken):

`sudo certbot renew`

- Simuleer het verkrijgen van een nieuw certificaat, maar sla deze niet op, op een harde schijf:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomein.voorbeeld.com</span>` --dry-run`

- Verkrijg een onvertrouwd test certificaat:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomein.voorbeeld.com</span>` --test-cert`
