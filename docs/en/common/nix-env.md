---
layout: page
title: common/nix-env (English)
description: "Manipulate or query Nix user environments."
content_hash: b10891ffcfafde98aa0249d09c844fe5c482dcd1
---
# nix-env

Manipulate or query Nix user environments.
More information: <https://nixos.org/manual/nix/stable/#sec-nix-env>.

- List all installed packages:

`nix-env -q`

- Query installed packages:

`nix-env -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Query available packages:

`nix-env -qa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Install package:

`nix-env -iA nixpkgs.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg_name</span>

- Install a package from a URL:

`nix-env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg_name</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Uninstall package:

`nix-env -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg_name</span>

- Upgrade one package:

`nix-env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg_name</span>

- Upgrade all packages:

`nix-env -u`
