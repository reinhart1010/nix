---
layout: page
title: common/acme.sh (português (Brasil))
description: "Script shell script que implementa o protocolo cliente ACME, ma alternativa para o certbot."
content_hash: d5a5ce828321b73240621503cef2ce6c787ccbba
last_modified_at: 2023-10-12
related_topics:
  - title: English version
    url: /en/common/acme.sh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acme.sh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># acme.sh

Script shell script que implementa o protocolo cliente ACME, ma alternativa para o certbot.
Veja também `acme.sh dns`.
Mais informações: <https://github.com/acmesh-official/acme.sh>.

- Emite um certificado usando o modo webroot:

`acme.sh --issue --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>` --webroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/webroot</span>

- Emite um certificado para múltiplos domínios usando o modo standalone na porta 80:

`acme.sh --issue --standalone --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.exemplo.com</span>

- Emite um certificado usando o modo standaline TLS na porta 443:

`acme.sh --issue --alpn --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Emite um certificado usando uma configuração válida Nginx:

`acme.sh --issue --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Emite um certificado usando uma configuração válida Apache:

`acme.sh --issue --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Emite um certificado wildcard (\*) usando o modo DNS_API automático:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.exemplo.com</span>

- Instala os arquivos dos certificaods em um local específico (útil para renovação automática do certificado):

`acme.sh --install-cert -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/exemplo.com.key</span>` --fullchain-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/caminho/para/exemplo.com.cer</span>` --reloadcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"systemctl force-reload nginx"</span>
