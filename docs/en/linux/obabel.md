---
layout: page
title: linux/obabel (English)
description: "Translate chemistry-related data."
content_hash: 09c003481f600ec92f98e38680e6ed885f663551
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# obabel

Translate chemistry-related data.
More information: <https://openbabel.org/wiki/Main_Page>.

- Convert a .mol file to XYZ coordinates:

`obabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mol</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xyz</span>

- Convert a SMILES string to a 500x500 picture:

`obabel -:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SMILES</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.png</span>` -xp 500`

- Convert a file of SMILES string to separate 3D .mol files:

`obabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.smi</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.mol</span>` --gen3D -m`

- Render multiple inputs into one picture:

`obabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.png</span>
