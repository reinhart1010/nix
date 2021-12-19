---
layout: page
title: common/yapf (English)
description: "Python style guide checker."
content_hash: 9cbc3b4f678c3b70cccc860e478d05fa3dfbfdf6
related_topics:
  - title: Nederlands version
    url: /nl/common/yapf.html
    icon: bi bi-globe
---
# yapf

Python style guide checker.
More information: <https://github.com/google/yapf>.

- Display a diff of the changes that would be made, without making them (dry-run):

`yapf --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Format the file in-place and display a diff of the changes:

`yapf --diff --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Recursively format all Python files in a directory, concurrently:

`yapf --recursive --in-place --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep8</span>` --parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
