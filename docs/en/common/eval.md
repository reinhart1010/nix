---
layout: page
title: common/eval (English)
description: "Execute arguments as a single command in the current shell and return its result."
content_hash: 0be5a54ed14d6c99f5fd68a2e5610037cf1f9d7c
last_modified_at: 2023-12-29
related_topics:
  - title: 中文 version
    url: /zh/common/eval.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eval

Execute arguments as a single command in the current shell and return its result.
More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#eval>.

- Call `echo` with the "foo" argument:

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo foo</span>`"`

- Set a variable in the current shell:

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo=bar</span>`"`
