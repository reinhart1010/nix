---
layout: page
title: linux/mopac (English)
description: "MOPAC (Molecular Orbital PACkage) is a semiempirical quantum chemistry program based on Dewar and Thiel's NDDO approximation."
content_hash: 2ca4ad97581f15af27a84374157b1e33b93945e3
last_modified_at: 2024-06-25
tldri18n_status: 2
---
# mopac

MOPAC (Molecular Orbital PACkage) is a semiempirical quantum chemistry program based on Dewar and Thiel's NDDO approximation.
More information: <https://github.com/openmopac/mopac>.

- Perform calculations according to an input file (`.mop`, `.dat`, and `.arc`):

`mopac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Minimal working example with HF that writes to the current directory and streams the output file:

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop & tail -f test.out`
