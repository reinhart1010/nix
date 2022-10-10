---
layout: page
title: common/git-stamp (English)
description: "Stamp the last commit message, with the possibility to reference the issues numbers from your bug tracker or link to its review page."
content_hash: f29710942b39d7a2c477bfdcc1ebe2e509da19f9
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git stamp

Stamp the last commit message, with the possibility to reference the issues numbers from your bug tracker or link to its review page.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-stamp>.

- Stamp the last commit message referencing it with the issue number from your bug tracker:

`git stamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>

- Stamp the last commit message linking it to its review page:

`git stamp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Review https://example.org/path/to/review</span>

- Stamp the last commit message replacing previous issues with a new one:

`git stamp --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">issue_number</span>
