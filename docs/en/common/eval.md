---
layout: page
title: common/eval (English)
description: "Execute arguments as a single command in the current shell and return its result."
content_hash: 5a46ccddd7cedae170d9814af40327ec17af67d7
related_topics:
  - title: 中文 version
    url: /zh/common/eval.html
    icon: bi bi-globe
---
# eval

Execute arguments as a single command in the current shell and return its result.
More information: <https://manned.org/eval>.

- Call `echo` with the "foo" argument:

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo foo</span>`"`

- Set a variable in the current shell:

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo=bar</span>`"`
