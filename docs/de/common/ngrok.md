---
layout: page
title: common/ngrok (Deutsch)
description: "Reverse-Proxy, welcher einen sicheren Tunnel von einem öffentlichen Endpunkt zu einem lokal verfügbaren Webservice erstellt."
content_hash: 7b8073d6065b9721baefeb3669837ff1da7ba6c4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ngrok.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ngrok

Reverse-Proxy, welcher einen sicheren Tunnel von einem öffentlichen Endpunkt zu einem lokal verfügbaren Webservice erstellt.
Weitere Informationen: <https://ngrok.com>.

- Veröffentliche einen lokalen HTTP-Service auf dem angegebenen Port:

`ngrok http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Veröffentliche einen lokalen HTTP-Service auf einem bestimmten Host:

`ngrok http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.dev</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- Veröffentliche einen lokalen HTTPS-Server:

`ngrok http https://localhost`

- Veröffentliche den TCP-Traffic auf dem angegebenen Port:

`ngrok tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- Veröffentliche den TLS-Traffic für einen bestimmten Host und Port:

`ngrok tls -hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.de</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>
