---
layout: page
title: common/nix-shell (Deutsch)
description: "Startet eine interaktive Shell, die auf einem Nix-Ausdruck basiert."
content_hash: 7714345a784576e9b57e7d6dce410019802f178c
last_modified_at: 2023-01-01
related_topics:
  - title: English version
    url: /en/common/nix-shell.html
    icon: bi bi-globe
---
# nix-shell

Startet eine interaktive Shell, die auf einem Nix-Ausdruck basiert.
Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-shell>.

- Starte mit Nix-Ausdruck in `shell.nix` oder `default.nix` im aktuellen Verzeichnis:

`nix-shell`

- Führe Shell-Befehl in nicht-interaktiver Shell aus und beende:

`nix-shell --run "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>`"`

- Starte mit Ausdruck in `default.nix` im aktuellen Verzeichnis:

`nix-shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default.nix</span>

- Starte mit aus nixpkgs geladenen Paketen:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name_1 paket_name_2 ...</span>

- Starte mit Paketen, die aus einer bestimmten Nixpkgs-Revision geladen wurden:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name_1 paket_name_2 ...</span>` -I nixpkgs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz</span>

- Führe den Rest der Datei mit einem bestimmten Interpreter aus, zur Verwendung in `#!-scripts` (siehe <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interpreter</span>` --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name_1 paket_name_2 ...</span>