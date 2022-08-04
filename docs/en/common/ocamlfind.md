---
layout: page
title: common/ocamlfind (English)
description: "The findlib package manager for OCaml."
content_hash: 35b261e84cf0208a95aeb430212cede3a560052b
---
# ocamlfind

The findlib package manager for OCaml.
Simplifies linking executables with external libraries.
More information: <http://projects.camlcity.org/projects/findlib.html>.

- Compile a source file to a native binary and link with packages:

`ocamlfind ocamlopt -package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package2</span>` -linkpkg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.ml</span>

- Compile a source file to a bytecode binary and link with packages:

`ocamlfind ocamlc -package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package2</span>` -linkpkg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.ml</span>

- Cross-compile for a different platform:

`ocamlfind -toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cross-toolchain</span>` ocamlopt -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.ml</span>
