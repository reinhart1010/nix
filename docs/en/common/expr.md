---
layout: page
title: common/expr (English)
description: "Evaluate expressions and manipulate strings."
content_hash: 3f8cd06df2232018cc9c7558c3b9148b0b777914
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/expr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/expr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/expr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expr

Evaluate expressions and manipulate strings.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html>.

- Get the length of a specific string:

`expr length "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`"`

- Get the substring of a string with a specific length:

`expr substr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">length</span>

- Match a specific substring against an anchored pattern:

`expr match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`'`

- Get the first char position from a specific set in a string:

`expr index "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chars</span>`"`

- Calculate a specific mathematic expression:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|*|/|%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression2</span>

- Get the first expression if its value is non-zero and not null otherwise get the second one:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression1</span>` \| `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression2</span>

- Get the first expression if both expressions are non-zero and not null otherwise get zero:

`expr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression1</span>` \& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression2</span>
