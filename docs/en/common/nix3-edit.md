---
layout: page
title: common/nix3-edit (English)
description: "Open the Nix expression of a Nix package in $EDITOR."
content_hash: e595dc97e16e6b3d2bc8ce0f69f077c69d431e3b
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix edit

Open the Nix expression of a Nix package in $EDITOR.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>.

- Open the source of the Nix expression of a package from nixpkgs in your `$EDITOR`:

`nix edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- Dump the source of a package to stdout:

`EDITOR=cat nix edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>
