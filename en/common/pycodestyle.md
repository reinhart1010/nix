---
layout: page
title: common/pycodestyle (English)
description: "A tool to check Python code against PEP 8 style conventions."
content_hash: a0fcdb4997d5d952ce35a251bb874e14343129b4
---
# pycodestyle

A tool to check Python code against PEP 8 style conventions.
More information: <https://pycodestyle.readthedocs.io>.

- Check the style of a single file:

`pycodestyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Check the style of multiple files:

`pycodestyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3.py</span>

- Show only the first occurrence of an error:

`pycodestyle --first `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Show the source code for each error:

`pycodestyle --show-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Show the specific PEP 8 text for each error:

`pycodestyle --show-pep8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>
