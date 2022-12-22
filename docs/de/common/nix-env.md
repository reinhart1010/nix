---
layout: page
title: common/nix-env (Deutsch)
description: "Manipulieren oder Abfragen von Nix-Benutzerumgebungen."
content_hash: 142b8415f7d3ce8ddf01ccd3a3f0729519ea6048
last_modified_at: 2022-12-22
related_topics:
  - title: English version
    url: /en/common/nix-env.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix-env

Manipulieren oder Abfragen von Nix-Benutzerumgebungen.
Weitere Informationen: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- Alle installierten Pakete auflisten:

`nix-env -q`

- Installierte Pakete abfragen:

`nix-env -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchbegriff</span>

- Verfügbare Pakete abfragen:

`nix-env -qa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchbegriff</span>

- Paket installieren:

`nix-env -iA nixpkgs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>

- Installieren eines Pakets von einer URL:

`nix-env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` --datei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beispiel.com</span>

- Paket deinstallieren:

`nix-env -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>

- Upgrade eines Pakets:

`nix-env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>

- Alle Pakete aktualisieren:

`nix-env -u`
