---
layout: page
title: common/yq (English)
description: "A lightweight and portable command-line YAML processor."
content_hash: c1731bf22d0ddea5575c14eac97e9e55adef35fc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# yq

A lightweight and portable command-line YAML processor.
More information: <https://mikefarah.gitbook.io/yq/>.

- Output a YAML file, in pretty-print format (v4+):

`yq eval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yaml</span>

- Output a YAML file, in pretty-print format (v3):

`yq read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yaml</span>` --colors`

- Output the first element in a YAML file that contains only an array (v4+):

`yq eval '.[0]' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yaml</span>

- Output the first element in a YAML file that contains only an array (v3):

`yq read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yaml</span>` '[0]'`

- Set (or overwrite) a key to a value in a file (v4+):

`yq eval '.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"' --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yaml</span>

- Set (or overwrite) a key to a value in a file (v3):

`yq write --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.yaml</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`'`

- Merge two files and print to `stdout` (v4+):

`yq eval-all 'select(filename == "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.yaml</span>`") * select(filename == "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.yaml</span>`")' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.yaml</span>

- Merge two files and print to `stdout` (v3):

`yq merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.yaml</span>` --colors`
