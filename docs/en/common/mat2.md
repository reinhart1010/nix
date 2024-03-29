---
layout: page
title: common/mat2 (English)
description: "Anonymise various file formats by removing metadata."
content_hash: 4864f6649334df9f077417d3e3894bdfe95e8787
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# mat2

Anonymise various file formats by removing metadata.
More information: <https://0xacab.org/jvoisin/mat2>.

- List supported file formats:

`mat2 --list`

- Remove metadata from a file:

`mat2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove metadata from a file and print detailed output to the console:

`mat2 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show metadata in a file without removing it:

`mat2 --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Partially remove metadata from a file:

`mat2 --lightweight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove metadata from a file in place, without creating a backup:

`mat2 --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
