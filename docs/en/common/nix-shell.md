---
layout: page
title: common/nix-shell (English)
description: "Start an interactive shell based on a Nix expression."
content_hash: 248c998f186aa51f6e92c22484b4401286a53045
last_modified_at: 2023-04-26
related_topics:
  - title: Deutsch version
    url: /de/common/nix-shell.html
    icon: bi bi-globe
---
# nix-shell

Start an interactive shell based on a Nix expression.
See also: `tldr nix3 shell`.
More information: <https://nixos.org/manual/nix/stable/command-ref/nix-shell.html>.

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
