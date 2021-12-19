---
layout: page
title: common/nasm (English)
description: "The Netwide Assembler, a portable 80x86 assembler."
content_hash: fe4fe1f63ed0a3d723b6126977fe20639445d347
---
# nasm

The Netwide Assembler, a portable 80x86 assembler.
More information: <https://nasm.us>.

- Assemble `source.asm` into a binary file `source`, in the (default) raw binary format:

`nasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>

- Assemble `source.asm` into a binary file `output_file`, in the specified format:

`nasm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- List valid output formats (along with basic nasm help):

`nasm -hf`

- Assemble and generate an assembly listing file:

`nasm -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>

- Add a directory (must be written with trailing slash) to the include file search path before assembling:

`nasm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/include_dir/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>
