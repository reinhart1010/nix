---
layout: page
title: common/black (English)
description: "A Python auto code formatter."
content_hash: 3091cf3da44c9f0b2eec0d245c4e0167546c13ae
related_topics:
  - title: italiano version
    url: /it/common/black.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/black.html
    icon: bi bi-globe
---
# black

A Python auto code formatter.
More information: <https://github.com/psf/black>.

- Auto-format a file or entire directory:

`black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Format the code passed in as a string:

`black -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>`"`

- Output the changes that would be applied for each file:

`black --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Perform a dry run (print what would be done without actually doing it):

`black --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Auto-format a file or directory emitting exclusively error messages to stderr:

`black --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Auto-format a file or directory without replacing single quotes with double quotes (adoption helper, avoid using this for new projects):

`black --skip-string-normalization `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>
