---
layout: page
title: common/cppclean (English)
description: "Find unused code in C++ projects."
content_hash: 7f6057577a416aa3072ec0d19eb581748117d39e
last_modified_at: 2024-04-19
related_topics:
  - title: فارسی version
    url: /fa/common/cppclean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cppclean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cppclean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cppclean

Find unused code in C++ projects.
More information: <https://github.com/myint/cppclean>.

- Run in a project's directory:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- Run on a project where the headers are in the `inc1/` and `inc2/` directories:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>` --include-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc1</span>` --include-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc2</span>

- Run on a specific file `main.cpp`:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main.cpp</span>

- Run on the current directory, excluding the "build" directory:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>
