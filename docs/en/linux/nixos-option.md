---
layout: page
title: linux/nixos-option (English)
description: "Inspect a NixOS configuration."
content_hash: f04b71941ba1713d6afd50293a6fc814298468aa
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nixos-option

Inspect a NixOS configuration.
More information: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- List all subkeys of a given option key:

`nixos-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_key</span>

- List current boot kernel modules:

`nixos-option boot.kernelModules`

- List authorized keys for a specific user:

`nixos-option users.users.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`.openssh.authorizedKeys.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyFiles|keys</span>

- List all remote builders:

`nixos-option nix.buildMachines`

- List all subkeys of a given key on another NixOS configuration:

`NIXOS_CONFIG=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path_to_configuration.nix</span>` nixos-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">option_key</span>

- Show recursively all values of a user:

`nixos-option -r users.users.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
