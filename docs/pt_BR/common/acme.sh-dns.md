---
layout: page
title: common/acme.sh-dns (português (Brasil))
description: "Usa um desafio DNS-01 para emitir um certificado TLS."
content_hash: 1735781283a7bed72dd513d2d3c8652b3a73adcf
last_modified_at: 2024-11-26
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
  - title: Indonesia version
    url: /id/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh-dns.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/acme.sh-dns.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># acme.sh --dns

Usa um desafio DNS-01 para emitir um certificado TLS.
Mais informações: <https://github.com/acmesh-official/acme.sh/wiki>.

- Emite um certificado usando um modo de DNS API automático:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnd_gd</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Emite um certificado wildcard (denotado por um asterísco (*)) usando um modo DNS API automático:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namesilo</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- Emite um certificado usando um modo apelido de DNS:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --challenge-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apelido-para-exemplo-de-validacao.com</span>

- Emite um certificado enquanto desabilita a pesquisa automática de DNS da Cloudflare/Google depois que o registro DNS for adicionado, especificando um tempo de espera personalizado em segundos:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namecheap</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --dnssleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- Emite um certificado usando o modo DNS manual:

`acme.sh --issue --dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --yes-I-know-dns-manual-mode-enough-go-ahead-please`
