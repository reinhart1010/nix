---
layout: page
title: common/zint (English)
description: "Generate barcodes and QR codes."
content_hash: bbf0c9f488d234675781a407b50bc5cb4a69813c
last_modified_at: 2024-06-02
tldri18n_status: 2
---
# zint

Generate barcodes and QR codes.
More information: <https://www.zint.org.uk/manual/chapter/4>.

- Generate a barcode and save it:

`zint --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8 data</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Specify a code type for generation:

`zint --barcode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code_type</span>` --data "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8 data</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List all supported code types:

`zint --types`
