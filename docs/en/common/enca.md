---
layout: page
title: common/enca (English)
description: "Detect and convert the encoding of text files."
content_hash: 32072fac7e38a98b41366cd8104798967d453edc
related_topics:
  - title: italiano version
    url: /it/common/enca.html
    icon: bi bi-globe
---
# enca

Detect and convert the encoding of text files.
More information: <https://github.com/nijel/enca>.

- Detect file(s) encoding according to the system's locale:

`enca `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Detect file(s) encoding specifying a language in the POSIX/C locale format (e.g. zh_CN, en_US):

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Convert file(s) to a specific encoding:

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Create a copy of an existing file using a different encoding:

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_encoding</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">original_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_file</span>
