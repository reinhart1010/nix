---
layout: page
title: common/funzip (English)
description: "Print the content of the first (non-directory) member in an archive without extraction."
content_hash: 08d59f74ee730372ff2607b95920d0c6fbab2eaf
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# funzip

Print the content of the first (non-directory) member in an archive without extraction.
More information: <https://manned.org/funzip>.

- Print the content of the first member in a Zip archive:

`funzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- Print the content in a gzip archive:

`funzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.gz</span>

- Decrypt a Zip or gzip archive and print the content:

`funzip -password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>
