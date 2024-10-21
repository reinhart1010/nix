---
layout: page
title: common/cdecl (English)
description: "Compose and decode C and C++ type declarations."
content_hash: 4180ef73a45ced3fb74603a0e7c2e3992cfa0814
last_modified_at: 2024-10-21
tldri18n_status: 2
---
# cdecl

Compose and decode C and C++ type declarations.
More information: <https://github.com/paul-j-lucas/cdecl>.

- Compose English phrase into C declaration, and create [c]ompilable output (include `;` and `{}`):

`cdecl -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phrase</span>

- Explain C declaration in English:

`cdecl explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C_declaration</span>

- Cast a variable to another type:

`cdecl cast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable_name</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>

- Run in [i]nteractive mode:

`cdecl -i`
