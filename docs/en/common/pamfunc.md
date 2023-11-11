---
layout: page
title: common/pamfunc (English)
description: "Apply a simple arithmetic function to a Netpbm image."
content_hash: 7d5f01f29377a02cb4045c506f75e3c0aa04672c
last_modified_at: 2023-11-11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pamfunc

Apply a simple arithmetic function to a Netpbm image.
More information: <https://netpbm.sourceforge.net/doc/pamfunc.html>.

- Apply the specified arithmetic function with `n` as the second argument to each sample in the specified PAM image:

`pamfunc -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">multiplier|divisor|adder|subtractor|min|max</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Apply the specified bit string function with `n` as the second argument to each sample in the specified PAM image:

`pamfunc -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">andmask|ormask|xormask|shiftleft|shiftright</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
