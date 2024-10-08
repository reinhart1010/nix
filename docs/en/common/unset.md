---
layout: page
title: common/unset (English)
description: "Remove shell variables or functions."
content_hash: 35bf28ef8d0f04d95cc7a12a582dc198e54dafee
last_modified_at: 2024-10-08
tldri18n_status: 2
---
# unset

Remove shell variables or functions.
More information: <https://manned.org/unset>.

- Remove the variable `foo`, or if the variable doesn't exist, remove the function `foo`:

`unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Remove the variables foo and bar:

`unset -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Remove the function my_func:

`unset -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_func</span>
