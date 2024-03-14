---
layout: page
title: linux/unzipsfx (English)
description: "Create a self-extracting compressed binary file by prepending self-extracting stubs on a Zip file."
content_hash: b17cd38b1cf671b3b144d78eff82c890b68ce863
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# unzipsfx

Create a self-extracting compressed binary file by prepending self-extracting stubs on a Zip file.
More information: <https://manned.org/unzipsfx>.

- Create a self-extracting binary file of a Zip archive:

`cat unzipsfx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` && chmod 755 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Extract a self-extracting binary in the current directory:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>

- Test a self-extracting binary for errors:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>` -t`

- Print content of a file in the self-extracting binary without extraction:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename</span>

- Print comments on Zip archive in the self-extracting binary:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./path/to/binary)</span>` -z`
