---
layout: page
title: common/autopep8 (English)
description: "Format Python code according to the PEP 8 style guide."
content_hash: 81f3a2683b8918f8813cbcedbfedc7582db27b37
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/autopep8.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autopep8.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/autopep8.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autopep8

Format Python code according to the PEP 8 style guide.
More information: <https://github.com/hhatto/autopep8>.

- Format a file to `stdout`, with a custom maximum line length:

`autopep8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>` --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">length</span>

- Format a file, displaying a diff of the changes:

`autopep8 --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format a file in-place and save the changes:

`autopep8 --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Recursively format all files in a directory in-place and save changes:

`autopep8 --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
