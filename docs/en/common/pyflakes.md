---
layout: page
title: common/pyflakes (English)
description: "Checks Python source code files for errors."
content_hash: 9ceab1e83ef9c31da5a829f1bb95b1b733cc2572
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# pyflakes

Checks Python source code files for errors.
More information: <https://pypi.org/project/pyflakes>.

- Check a single Python file:

`pyflakes check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Check Python files in a specific directory:

`pyflakes checkPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Check Python files in a directory recursively:

`pyflakes checkRecursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Check all Python files found in multiple directories:

`pyflakes iterSourceCode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_2</span>
