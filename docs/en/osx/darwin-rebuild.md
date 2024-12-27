---
layout: page
title: osx/darwin-rebuild (English)
description: "Rebuild and switch to a Nix-based Darwin (macOS) system configuration."
content_hash: 23a017758ad9a8ca9371600d0b35e9549e1515be
last_modified_at: 2024-12-27
tldri18n_status: 2
---
# darwin-rebuild

Rebuild and switch to a Nix-based Darwin (macOS) system configuration.
More information: <https://github.com/LnL7/nix-darwin>.

- Rebuild and switch to the specified Darwin configuration:

`darwin-rebuild switch --flake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/flake</span>

- Build the configuration but don't switch to it:

`darwin-rebuild build --flake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/flake</span>

- Display help:

`darwin-rebuild --help`
