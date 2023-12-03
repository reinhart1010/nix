---
layout: page
title: common/acme.sh (Nederlands)
description: "Shell-script dat het ACME-clientprotocol implementeert, een alternatief voor `certbot`."
content_hash: ffe2e1ef749c9ae3117e575e73243e8b455aaad0
last_modified_at: 2023-12-03
related_topics:
  - title: বাংলা version
    url: /bn/common/acme.sh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/acme.sh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acme.sh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/acme.sh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acme.sh

Shell-script dat het ACME-clientprotocol implementeert, een alternatief voor `certbot`.
Zie ook `acme.sh dns`.
Meer informatie: <https://github.com/acmesh-official/acme.sh>.

- Geef een certificaat uit met behulp van de webroot-modus:

`acme.sh --issue --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --webroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/webroot</span>

- Geef een certificaat uit voor meerdere domeinen in de zelfstandige modus met poort 80:

`acme.sh --issue --standalone --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.voorbeeld.com</span>

- Geef een certificaat uit met behulp van de zelfstandige TLS-modus met behulp van poort 443:

`acme.sh --issue --alpn --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>

- Geef een certificaat uit met een werkende Nginx-configuratie:

`acme.sh --issue --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>

- Geef een certificaat uit met een werkende Apache-configuratie:

`acme.sh --issue --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>

- Geef een wildcardcertificaat (\*) uit met behulp van een automatische DNS API-modus:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.voorbeeld.com</span>

- Installeer certificaatbestanden op de opgegeven locaties (handig voor automatische certificaatvernieuwing):

`acme.sh --install-cert -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/voorbeeld.com.key</span>` --fullchain-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/voorbeeld.com.cer</span>` --reloadcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"systemctl force-reload nginx"</span>
