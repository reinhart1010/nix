---
layout: page
title: common/choose (English)
description: "A human-friendly and fast alternative to cut and (sometimes) awk."
content_hash: a7297692eae0dd056b8f77a01cf715e20239740a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# choose

A human-friendly and fast alternative to cut and (sometimes) awk.
More information: <https://github.com/theryangeary/choose>.

- Print the 5th item from a line (starting from 0):

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Print the first, 3rd, and 5th item from a line, where items are separated by ':' instead of whitespace:

`choose --field-separator '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Print everything from the 2nd to 5th item on the line, including the 5th:

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Print everything from the 2nd to 5th item on the line, excluding the 5th:

`choose --exclusive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Print the beginning of the line to the 3rd item:

`choose :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Print all items from the beginning of the line until the 3rd item (exclusive):

`choose --exclusive :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Print all items from the 3rd to the end of the line:

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>`:`

- Print the last item from a line:

`choose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>
