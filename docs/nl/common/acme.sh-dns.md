---
layout: page
title: common/acme.sh-dns (Nederlands)
description: "Gebruik een DNS-01 challenge om een TLS-certificaat uit te geven."
content_hash: f5df6f9612f9b92f6fe639289288e55028d77c05
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh-dns.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acme.sh --dns

Gebruik een DNS-01 challenge om een TLS-certificaat uit te geven.
Meer informatie: <https://github.com/acmesh-official/acme.sh/wiki>.

- Geef een certificaat uit met behulp van een automatische DNS API-modus:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnd_gd</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>

- Geef een wildcardcertificaat uit (aangegeven met een asterisk) met behulp van een automatische DNS API-modus:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namesilo</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.voorbeeld.com</span>

- Geef een certificaat uit met behulp van een DNS-aliasmodus:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --challenge-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias-voor-voorbeeld-validatie.com</span>

- Geef een certificaat uit terwijl u automatische Cloudflare / Google DNS-polling uitschakelt nadat het DNS-record is toegevoegd door een aangepaste wachttijd in seconden op te geven:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namecheap</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --dnssleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- Geef een certificaat uit met behulp van een handmatige DNS-modus:

`acme.sh --issue --dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --yes-I-know-dns-manual-mode-enough-go-ahead-please`
