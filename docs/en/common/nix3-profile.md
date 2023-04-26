---
layout: page
title: common/nix3-profile (English)
description: "Install, update and remove packages from Nix profiles."
content_hash: 0474d49d9684e4948ff6295b29055bfd7764121a
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix profile

Install, update and remove packages from Nix profiles.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-profile.html>.

- Install some packages from nixpkgs into the default profile:

`nix profile install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg1 nixpkgs#pkg2 ...</span>

- Install a package from a flake on GitHub into a custom profile:

`nix profile install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:owner/repo/pkg</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/directory</span>

- List packages currently installed in the default profile:

`nix profile list`

- Remove a package installed from nixpkgs from the default profile, by name:

`nix profile remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legacyPackages.x86_64-linux.pkg</span>

- Upgrade packages in the default to the latest available versions:

`nix profile upgrade`

- Rollback (cancel) the latest action on the default profile:

`nix profile rollback`
