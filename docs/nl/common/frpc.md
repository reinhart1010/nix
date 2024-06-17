---
layout: page
title: common/frpc (Nederlands)
description: "Maak verbinding met een `frps`-server om verbindingen op de huidige host te proxyen."
content_hash: 6df122faddf0e10d550381339fcc435191e7c33e
last_modified_at: 2024-06-17
related_topics:
  - title: English version
    url: /en/common/frpc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# frpc

Maak verbinding met een `frps`-server om verbindingen op de huidige host te proxyen.
Onderdeel van `frp`.
Meer informatie: <https://github.com/fatedier/frp>.

- Start de service met het standaardconfiguratiebestand (aangenomen wordt dat dit `frps.ini` is in de huidige map):

`frpc`

- Start de service met het nieuwere TOML-configuratiebestand (`frps.toml` in plaats van `frps.ini`) in de huidige map:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Start de service met een specifiek configuratiebestand:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Controleer of het configuratiebestand geldig is:

`frpc verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon het script om autocompletion op te zetten voor Bash, fish, PowerShell of Zsh:

`frpc completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Toon de versie:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
