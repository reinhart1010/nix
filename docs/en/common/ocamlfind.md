---
layout: page
title: common/ocamlfind (English)
description: "The findlib package manager for OCaml."
content_hash: 1eb5d6968d6cd395c5523646ad9da76b02159912
last_modified_at: 2023-05-19
---
# ocamlfind

The findlib package manager for OCaml.
Simplifies linking executables with external libraries.
More information: <http://projects.camlcity.org/projects/findlib.html>.

- Compile a source file to a native binary and link with packages:

`ocamlfind ocamlopt -package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package2</span>` -linkpkg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.ml</span>

- Compile a source file to a bytecode binary and link with packages:

`ocamlfind ocamlc -package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package2</span>` -linkpkg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.ml</span>

- Cross-compile for a different platform:

`ocamlfind -toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cross-toolchain</span>` ocamlopt -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.ml</span>
