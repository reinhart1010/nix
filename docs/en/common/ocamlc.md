---
layout: page
title: common/ocamlc (English)
description: "The OCaml bytecode compiler."
content_hash: dd8cc4f8ab29cce5c384e43e6f020601f8eba257
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ocamlc

The OCaml bytecode compiler.
Produces executables runnable by the OCaml interpreter.
More information: <https://ocaml.org>.

- Create a binary from a source file:

`ocamlc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.ml</span>

- Create a named binary from a source file:

`ocamlc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.ml</span>

- Automatically generate a module signature (interface) file:

`ocamlc -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.ml</span>
