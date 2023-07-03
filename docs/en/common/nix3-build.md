---
layout: page
title: common/nix3-build (English)
description: "Build a Nix expression (downloading from the cache when possible)."
content_hash: e30cb276279ccb6d6465e3f79ea18ffbc8fff8df
last_modified_at: 2023-07-03
---
# nix build

Build a Nix expression (downloading from the cache when possible).
See also: `tldr nix-build`. See `tldr nix3 flake` for information about flakes.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-build.html>.

- Build a package from nixpkgs, symlinking the result to `./result`:

`nix build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- Build a package from a flake in the current directory, showing the build logs in the process:

`nix build -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.#pkg</span>

- Build the default package from a flake in some directory:

`nix build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/directory</span>

- Build a package without making the `result` symlink, instead printing the store path to the `stdout`:

`nix build --no-link --print-out-paths`
