---
layout: page
title: common/nix3-shell (English)
description: "Start a shell in which the specified packages are available."
content_hash: af21f2c3f0fe6f90b5df2b6d4713ce057db54161
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix shell

Start a shell in which the specified packages are available.
See also: `tldr nix-shell`. See `tldr nix3 flake` for information about flakes.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-shell.html>.

- Start an interactive shell with some packages from `nixpkgs`:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...</span>

- Start a shell providing a package from an older version of `nixpkgs` (21.05):

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs/nixos-21.05#pkg</span>

- Start a shell with the "default package" from a flake in the current directory, printing build logs if any builds happen:

`nix shell -L`

- Start a shell with a package from a flake on GitHub:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:owner/repo#pkg</span>

- Run a command in a shell with a package:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some-cmd --someflag 'Some other arguments'</span>
