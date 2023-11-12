---
layout: page
title: common/afconvert (English)
description: "Convert between AFF and raw file formats."
content_hash: 78e7b495bcad4730a9f688d78df5aaa99949b3cf
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/afconvert.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/afconvert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/afconvert.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/afconvert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afconvert

Convert between AFF and raw file formats.
More information: <https://manned.org/afconvert.1>.

- Use a specific extension (default: `aff`):

`afconvert -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">extension</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file1 path/to/output_file2 ...</span>

- Use a specific compression level (default: `7`):

`afconvert -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file1 path/to/output_file2 ...</span>
