---
layout: page
title: common/home-manager (English)
description: "Manage a per-user environment using Nix, allowing declarative configuration of the user’s home."
content_hash: 1edb90000d321494044a8faeae214a2f1432e499
last_modified_at: 2024-12-27
related_topics:
  - title: 한국어 version
    url: /ko/common/home-manager.html
    icon: bi bi-globe
tldri18n_status: 2
---
# home-manager

Manage a per-user environment using Nix, allowing declarative configuration of the user’s home.
More information: <https://github.com/nix-community/home-manager>.

- Build the configuration defined in `~/.config/nixpkgs/home.nix` without applying it:

`home-manager build`

- Build and apply (switch to) the new configuration:

`home-manager switch`

- Build the configuration for testing without applying it:

`home-manager test`

- Roll back to a previous configuration generation:

`home-manager rollback`

- List all existing configuration generations:

`home-manager generations`
