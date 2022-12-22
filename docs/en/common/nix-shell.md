---
layout: page
title: common/nix-shell (English)
description: "Start an interactive shell based on a Nix expression."
content_hash: 01985d44d71524c80f01e3cf11882c491712caf5
last_modified_at: 2022-12-22
---
# nix-shell

Start an interactive shell based on a Nix expression.
More information: <https://nixos.org/manual/nix/stable/#sec-nix-shell>.

- Start with nix expression in `shell.nix` or `default.nix` in the current directory:

`nix-shell`

- Run shell command in non-interactive shell and exit:

`nix-shell --run "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>`"`

- Start with expression in `default.nix` in the current directory:

`nix-shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default.nix</span>

- Start with packages loaded from nixpkgs:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name_1 package_name_2 ...</span>

- Start with packages loaded from specific nixpkgs revision:

`nix-shell --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name_1 package_name_2 ...</span>` -I nixpkgs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz</span>

- Evaluate rest of file in specific interpreter, for use in `#!-scripts` (see <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interpreter</span>` --packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name_1 package_name_2 ...</span>
