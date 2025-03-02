---
layout: page
title: common/local (English)
description: "Declare local variables and give them attributes."
content_hash: e7d29b58a7750c9c3218f2e3f4e8aa3de07d8ff0
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/local.html
    icon: bi bi-globe
tldri18n_status: 2
---
# local

Declare local variables and give them attributes.
See also: `declare`.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-local>.

- Declare a string variable with the specified value:

`local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Declare an integer variable with the specified value:

`local -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Declare an array variable with the specified value:

`local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_a item_b item_c</span>`)`

- Declare an associative array variable with the specified value:

`local -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[key_a]=item_a [key_b]=item_b [key_c]=item_c</span>`)`

- Declare a readonly variable with the specified value:

`local -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`
