---
layout: page
title: common/cppcheck (English)
description: "A static analysis tool for C/C++ code."
content_hash: e5ce98972481c41dd4d5ec887d114acb2832644f
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/cppcheck.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cppcheck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cppcheck

A static analysis tool for C/C++ code.
Instead of syntax errors, it focuses on the types of bugs that compilers normally do not detect.
More information: <http://cppcheck.sourceforge.net>.

- Recursively check the current directory, showing progress on the screen and logging error messages to a file:

`cppcheck . 2> cppcheck.log`

- Recursively check a given directory, and don't print progress messages:

`cppcheck --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Check a given file, specifying which tests to perform (by default only errors are shown):

`cppcheck --enable=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error|warning|style|performance|portability|information|all</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- List available tests:

`cppcheck --errorlist`

- Check a given file, ignoring specific tests:

`cppcheck --suppress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_id1</span>` --suppress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_id2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.cpp</span>

- Check the current directory, providing paths for include files located outside it (e.g. external libraries):

`cppcheck -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">include/directory_1</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">include/directory_2</span>` .`

- Check a Microsoft Visual Studio project (`*.vcxproj`) or solution (`*.sln`):

`cppcheck --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project.sln</span>
