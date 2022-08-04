---
layout: page
title: common/yacas (English)
description: "Yet Another Computer Algebra System."
content_hash: 163a51629f70f49c879f81f319e2a3ca8ace5e62
---
# yacas

Yet Another Computer Algebra System.
More information: <http://www.yacas.org>.

- Start an interactive `yacas` session:

`yacas`

- While in a `yacas` session, execute a statement:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Integrate(x)Cos(x)</span>`;`

- While in a `yacas` session, display an example:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example()</span>`;`

- Quit from a `yacas` session:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quit</span>

- Execute one or more `yacas` scripts (without terminal or prompts), then exit:

`yacas -p -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script2</span>

- Execute and print the result of one statement, then exit:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Echo( Deriv(x)Cos(1/x) );</span>`" | yacas -p -c /dev/stdin`
