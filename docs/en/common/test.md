---
layout: page
title: common/test (English)
description: "Check file types and compare values."
content_hash: 27338450b425a84354881c6e87b46efe64115fa3
last_modified_at: 2025-03-02
related_topics:
  - title: 日本語 version
    url: /ja/common/test.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/test.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/test.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# test

Check file types and compare values.
Returns 0 if the condition evaluates to true, 1 if it evaluates to false.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

- Test if a given variable is equal to a given string:

`test "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$MY_VAR</span>`" = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/zsh</span>`"`

- Test if a given variable is empty:

`test -z "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GIT_BRANCH</span>`"`

- Test if a file exists:

`test -f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>`"`

- Test if a directory does not exist:

`test ! -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`"`

- If A is true, then do B, or C in the case of an error (notice that C may run even if A fails):

`test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">condition</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "true"</span>` || `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "false"</span>
