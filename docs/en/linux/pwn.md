---
layout: page
title: linux/pwn (English)
description: "Exploit Development Library designed for rapid prototyping."
content_hash: 1d2d98cfdf5beea8963ef9bbd961f8765476fcbf
last_modified_at: 2024-03-03
tldri18n_status: 2
---
# pwn

Exploit Development Library designed for rapid prototyping.
More information: <https://docs.pwntools.com/en/stable/commandline.html>.

- Convert the given assembly code to `bytes`:

`pwn asm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xor edi, edi</span>`"`

- Create a cyclic pattern of the specific number of characters:

`pwn cyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Encode the given data into the hexadecimal system:

`pwn hex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deafbeef</span>

- Decode the given data from hexadecimal:

`pwn unhex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6c4f7645</span>

- Print a x64 Linux shellcode for running a shell:

`pwn shellcraft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amd64.linux.sh</span>

- Check the binary security settings for the given ELF file:

`pwn checksec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check for Pwntools updates:

`pwn update`

- Display version:

`pwn version`
