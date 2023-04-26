---
layout: page
title: common/nix3-run (English)
description: "Run an application from a Nix flake."
content_hash: f13b4384a30895556bca18dc7635c2f965f61082
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix run

Run an application from a Nix flake.
See `tldr nix3 flake` for information about flakes.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>.

- Run a command whose name matches the package name from nixpkgs (if you want a different command from that package, see `tldr nix3 shell`):

`nix run nixpkgs#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg</span>

- Run the default application in the flake in the current directory:

`nix run`
