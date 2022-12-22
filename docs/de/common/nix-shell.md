---
layout: page
title: common/nix-shell (Deutsch)
description: "Startet eine interaktive Shell, die auf einem Nix-Ausdruck basiert."
content_hash: 727ab1633fd46ffe4ec0e5c4f139ee2f72ead4a5
last_modified_at: 2022-12-22
related_topics:
  - title: English version
    url: /en/common/nix-shell.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix-shell

Startet eine interaktive Shell, die auf einem Nix-Ausdruck basiert.
Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-shell>.

- Start mit Nix-Ausdruck in `shell.nix` oder `default.nix` im aktuellen Verzeichnis:

`nix-shell`

- Shell-Befehl in nicht-interaktiver Shell ausführen und beenden:

`nix-shell --run "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>`"`

- Start mit Ausdruck in `default.nix` im aktuellen Verzeichnis:

`nix-shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default.nix</span>

- Start mit aus nixpkgs geladenen Paketen:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name_1 paket_name_2 ...</span>

- Start mit Paketen, die aus einer bestimmten Nixpkgs-Revision geladen wurden:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name_1 paket_name_2 ...</span>` -I nixpkgs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz</span>

- Den Rest der Datei mit einem bestimmten Interpreter auswerten, zur Verwendung in `#!-scripts` (siehe <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interpreter</span>` --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name_1 paket_name_2 ...</span>
