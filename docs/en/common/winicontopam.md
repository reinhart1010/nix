---
layout: page
title: common/winicontopam (English)
description: "Convert a Windows ICO file to a PAM file."
content_hash: aef52e409aeaf5432f5980c6108c825196bdaaed
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# winicontopam

Convert a Windows ICO file to a PAM file.
More information: <https://netpbm.sourceforge.net/doc/winicontopam.html>.

- Read an ICO file and convert the best quality image contained therein to the PAM format:

`winicontopam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Convert all images in the input file to PAM:

`winicontopam -allimages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Convert the n'th image in the input file to PAM:

`winicontopam -image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- If the image(s) to be extracted contain graded transparency data and an AND mask, write the AND mask into the fifth channel of the output PAM file:

`winicontopam -andmasks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
