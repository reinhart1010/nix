---
layout: page
title: common/nix3-repl (English)
description: "Start an interactive environment for evaluating Nix expressions."
content_hash: f175a608ef81fd177d6f8cb7a1523f66e15a9068
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nix repl

Start an interactive environment for evaluating Nix expressions.
See <https://nixos.org/manual/nix/stable/language/index.html> for a description of the Nix expression language.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-repl.html>.

- Start an interactive environment for evaluating Nix expressions:

`nix repl`

- Load all packages from a flake (e.g. `nixpkgs`) into scope:

`:lf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs</span>

- Build a package from an expression:

`:b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>

- Start a shell with package from the expression available:

`:u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>

- Start a shell with dependencies of the package from the expression available:

`:s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>
