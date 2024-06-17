---
layout: page
title: common/frps (Nederlands)
description: "Stel snel een reverse proxy-service in."
content_hash: b544affb705cf18e41100267bd3a734cc6777eb8
last_modified_at: 2024-06-17
related_topics:
  - title: English version
    url: /en/common/frps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# frps

Stel snel een reverse proxy-service in.
Onderdeel van `frp`.
Meer informatie: <https://github.com/fatedier/frp>.

- Start de service met het standaardconfiguratiebestand (aangenomen wordt dat dit `frps.ini` is in de huidige map):

`frps`

- Start de service met het nieuwere TOML-configuratiebestand (`frps.toml` in plaats van `frps.ini`) in de huidige map:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Start de service met een specifiek configuratiebestand:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Controleer of het configuratiebestand geldig is:

`frps verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon het script om autocompletion op te zetten voor Bash, fish, PowerShell of Zsh:

`frps completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Toon de versie:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
