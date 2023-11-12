---
layout: page
title: linux/certbot (English)
description: "The Let's Encrypt Agent for automatically obtaining and renewing TLS certificates."
content_hash: 01e740dd97e3c61d96cec396d3ab2428b61f66b5
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/certbot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/certbot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/certbot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certbot

The Let's Encrypt Agent for automatically obtaining and renewing TLS certificates.
Successor to `letsencrypt`.
More information: <https://certbot.eff.org/docs/using.html>.

- Obtain a new certificate via webroot authorization, but do not install it automatically:

`sudo certbot certonly --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.example.com</span>

- Obtain a new certificate via nginx authorization, installing the new certificate automatically:

`sudo certbot --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.example.com</span>

- Obtain a new certificate via apache authorization, installing the new certificate automatically:

`sudo certbot --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.example.com</span>

- Renew all Let's Encrypt certificates that expire in 30 days or less (don't forget to restart any servers that use them afterwards):

`sudo certbot renew`

- Simulate the obtaining of a new certificate, but don't actually save any new certificates to disk:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.example.com</span>` --dry-run`

- Obtain an untrusted test certificate instead:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/webroot</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain.example.com</span>` --test-cert`
