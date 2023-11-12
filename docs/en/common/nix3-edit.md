---
layout: page
title: common/nix3-edit (English)
description: "Open the Nix expression of a Nix package in $EDITOR."
content_hash: 27400a2ff8ef3869a5a4ff747e147db88b5ce7fd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nix edit

Open the Nix expression of a Nix package in $EDITOR.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>.

- Open the source of the Nix expression of a package from nixpkgs in your `$EDITOR`:

`nix edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- Dump the source of a package to `stdout`:

`EDITOR=cat nix edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>
