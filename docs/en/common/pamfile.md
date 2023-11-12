---
layout: page
title: common/pamfile (English)
description: "Describe Netpbm (PAM or PNM) files."
content_hash: 0f4b27cd94254d7327e4c8656b3ca33de43ca712
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pamfile

Describe Netpbm (PAM or PNM) files.
More information: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- Describe the specified Netpbm files:

`pamfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Describe every image in each input file (as opposed to only the first image in each file) in a machine-readable format:

`pamfile -allimages -machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display a count on how many images the input files contain:

`pamfile -count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
