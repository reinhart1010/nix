---
layout: page
title: common/csv2tsv (English)
description: "Convert CSV (comma-separated) text to TSV (tab-separated) format."
content_hash: cad7106bc5ff3c1ab375f754ef2613ee99fcb4bb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# csv2tsv

Convert CSV (comma-separated) text to TSV (tab-separated) format.
More information: <https://github.com/eBay/tsv-utils/blob/master/README.md#csv2tsv>.

- Convert from CSV to TSV:

`csv2tsv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_csv1 path/to/input_csv2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_tsv</span>

- Convert field delimiter separated CSV to TSV:

`csv2tsv -c'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">field_delimiter</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_csv</span>

- Convert semicolon separated CSV to TSV:

`csv2tsv -c';' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_csv</span>
