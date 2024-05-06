---
layout: page
title: linux/nixos-container (Deutsch)
description: "Startet NixOS Container basierend auf Linux Containern."
content_hash: 249dd71b04c3d905a828f0bf37f366eeef52a43f
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/linux/nixos-container.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nixos-container

Startet NixOS Container basierend auf Linux Containern.
Weitere Informationen: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- Gibt eine Liste der gestarteten Container aus:

`sudo nixos-container list`

- Erstelle einen NixOS Container mit einer spezifischen Konfigurations-Datei:

`sudo nixos-container create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nix_config_file_path</span>

- Starte, stoppe, terminiere oder zerstöre den angegebenen Container:

`sudo nixos-container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|terminate|destroy|status</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Führe ein Kommando in einem laufenden Container aus:

`sudo nixos-container run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Aktualisiere eine Containerkonfiguration:

`sudo $EDITOR /var/lib/container/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`/etc/nixos/configuration.nix && sudo nixos-container update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Starte eine interaktive Shell innerhalb eines laufenden Containers:

`sudo nixos-container root-login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
