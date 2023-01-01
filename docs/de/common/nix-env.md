---
layout: page
title: common/nix-env (Deutsch)
description: "Manipulieren oder Abfragen von Nix-Benutzerumgebungen."
content_hash: 8898b3a4212cddcdc08181cb62b13b8eb07bb3d8
last_modified_at: 2023-01-01
related_topics:
  - title: English version
    url: /en/common/nix-env.html
    icon: bi bi-globe
---
# nix-env

Manipulieren oder Abfragen von Nix-Benutzerumgebungen.
Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- Liste alle installierten Pakete auf:

`nix-env -q`

- Frage installierte Pakete ab:

`nix-env -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchbegriff</span>

- Frage verfügbare Pakete ab:

`nix-env -qa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchbegriff</span>

- Installiere Paket:

`nix-env -iA nixpkgs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>

- Installiere ein Paket von einer URL:

`nix-env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` --datei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Deinstalliere Paket:

`nix-env -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>

- Upgrade ein Pakets:

`nix-env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>

- Upgrade alle Pakete:

`nix-env -u`
