---
layout: page
title: linux/nixos-option (Deutsch)
description: "Prüfe eine NixOS Konfiguration."
content_hash: 90f578aaef320ccf192c05cfd6002b703bc55de3
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/linux/nixos-option.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nixos-option

Prüfe eine NixOS Konfiguration.
Weitere Informationen: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- Liste alle Unterschlüssel eines angegebenen Options-Schlüssels:

`nixos-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_key</span>

- Liste aktuelle Boot-Kernelmodule:

`nixos-option boot.kernelModules`

- Liste Authorisierungsschlüssel für einen spezifischen Benutzer:

`nixos-option users.users.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`.openssh.authorizedKeys.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyFiles|keys</span>

- Liste alle Remote-Builder-Maschinen:

`nixos-option nix.buildMachines`

- Liste alle Unterschlüssel eines angegebenen Options-Schlüssels innerhalb einer angegebenen Konfigurations-Datei:

`NIXOS_CONFIG=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path_to_configuration.nix</span>` nixos-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_key</span>

- Zeige rekursiv alle Werte eines Benutzers:

`nixos-option -r users.users.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
