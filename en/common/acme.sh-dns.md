---
layout: page
title: common/acme.sh-dns (English)
description: "Use a DNS-01 challenge to issue a TLS certificate."
content_hash: b79e0894a4b97f7161bf618bf34b52ee1cfcf4ae
---
# acme.sh --dns

Use a DNS-01 challenge to issue a TLS certificate.
More information: <https://github.com/acmesh-official/acme.sh/wiki>.

- Issue a certificate using an automatic DNS API mode:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnd_gd</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Issue a wildcard certificate (denoted by an asterisk) using an automatic DNS API mode:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namesilo</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- Issue a certificate using a DNS alias mode:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --challenge-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias-for-example-validation.com</span>

- Issue a certificate while disabling automatic Cloudflare / Google DNS polling after the DNS record is added by specifying a custom wait time in seconds:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namecheap</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --dnssleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- Issue a certificate using a manual DNS mode:

`acme.sh --issue --dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --yes-I-know-dns-manual-mode-enough-go-ahead-please`
