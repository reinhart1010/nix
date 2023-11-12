---
layout: page
title: common/funzip (English)
description: "Print the content of the first (non-directory) member in an archive without extraction."
content_hash: 980a8907cf8b1a81554ee288464eca3a6b699bdb
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# funzip

Print the content of the first (non-directory) member in an archive without extraction.
More information: <https://manned.org/funzip>.

- Print the content of the first member in a `.zip` archive:

`funzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- Print the content in a `.gz` archive:

`funzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.gz</span>

- Decrypt a `.zip` or `.gz` archive and print the content:

`funzip -password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive</span>
