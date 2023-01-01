---
layout: page
title: common/afconvert (English)
description: "Convert between AFF and raw file formats."
content_hash: 78e7b495bcad4730a9f688d78df5aaa99949b3cf
last_modified_at: 2023-01-01
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># afconvert

Convert between AFF and raw file formats.
More information: <https://manned.org/afconvert.1>.

- Use a specific extension (default: `aff`):

`afconvert -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file1 path/to/output_file2 ...</span>

- Use a specific compression level (default: `7`):

`afconvert -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file1 path/to/output_file2 ...</span>
