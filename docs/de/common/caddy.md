---
layout: page
title: common/caddy (Deutsch)
description: "Ein unternehmenstauglicher Open-Source-Webserver mit automatischem HTTPS, geschrieben in Go."
content_hash: e293e3125cbe39146ab780dfdbbb40acdfb112ce
last_modified_at: 2023-10-22
related_topics:
  - title: English version
    url: /en/common/caddy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/caddy.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caddy

Ein unternehmenstauglicher Open-Source-Webserver mit automatischem HTTPS, geschrieben in Go.
Weitere Informationen: <https://caddyserver.com>.

- Starte Caddy im Vordergrund:

`caddy run`

- Starte Caddy mit dem angegebenen Caddyfile:

`caddy run --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/Caddyfile</span>

- Starte Caddy im Hintergrund:

`caddy start`

- Stoppe einen im Hintergrund laufenden Caddy-Prozess:

`caddy stop`

- Führe einen einfachen Dateiserver auf dem angegebenen Port mit einer durchsuchbaren Oberfläche aus:

`caddy file-server --listen :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --browse`

- Führe einen Reverse-Proxy-Server aus:

`caddy reverse-proxy --from :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --to localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>
