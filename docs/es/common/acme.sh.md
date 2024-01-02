---
layout: page
title: common/acme.sh (español)
description: "Shell script implementando el protocolo cliente ACME, una alternativa a `certbot`."
content_hash: 615c8d95965b1b6051677ada72bfb6d057861e94
last_modified_at: 2024-01-02
related_topics:
  - title: বাংলা version
    url: /bn/common/acme.sh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/acme.sh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acme.sh.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/acme.sh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh.html
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

Shell script implementando el protocolo cliente ACME, una alternativa a `certbot`.
Ver también `acme.sh dns`.
Más información: <https://github.com/acmesh-official/acme.sh>.

- Emite un certificado usando el modo webroot:

`acme.sh --issue --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` --webroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/webroot</span>

- Emite un certificado para múltiples dominios utilizando el modo autónomo a través del puerto 80:

`acme.sh --issue --standalone --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.ejemplo.com</span>

- Emite un certificado en modo autónomo TLS utilizando el puerto 443:

`acme.sh --issue --alpn --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Emite un certificado utilizando una configuración de Nginx operativa:

`acme.sh --issue --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Emite un certificado utilizando una configuración de Apache operativa:

`acme.sh --issue --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Emite un certificado comodín (\*) utilizando un modo API DNS automático:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ejemplo.com</span>

- Instala archivos de certificado en las ubicaciones especificadas (útil para la renovación automática de certificados):

`acme.sh --install-cert -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/ejemplo.com.key</span>` --fullchain-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/ejemplo.com.cer</span>` --reloadcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"systemctl force-reload nginx"</span>
