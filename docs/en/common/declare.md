---
layout: page
title: common/declare (English)
description: "Declare variables and give them attributes."
content_hash: db736e7a68742fe686468329e5ba45883970627a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# declare

Declare variables and give them attributes.
More information: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Declare a string variable with the specified value:

`declare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Declare an integer variable with the specified value:

`declare -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Declare an array variable with the specified value:

`declare -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_a item_b item_c</span>`)`

- Declare an associative array variable with the specified value:

`declare -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[key_a]=item_a [key_b]=item_b [key_c]=item_c</span>`)`

- Declare a readonly string variable with the specified value:

`declare -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- Declare a global variable within a function with the specified value:

`declare -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`
