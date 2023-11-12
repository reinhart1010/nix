---
layout: page
title: common/pdfjoin (English)
description: "PDF merging utility based on pdfjam."
content_hash: 6298dd6db75f0a97113350a9fa59f679a818eff3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pdfjoin

PDF merging utility based on pdfjam.
More information: <https://github.com/rrthomas/pdfjam-extras>.

- Merge two PDFs into one with the default suffix "joined":

`pdfjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.pdf</span>

- Merge the first page of each given file together:

`pdfjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pdf path/to/file2.pdf ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- Save pages 3 to 5 followed by page 1 to a new PDF with custom suffix:

`pdfjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-5,1</span>` --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rearranged</span>

- Merge page subranges from two PDFs:

`pdfjoin {/path/to/file1.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last-3</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>
