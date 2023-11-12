---
layout: page
title: common/shc (English)
description: "Generic shell script compiler."
content_hash: 68295f672b3fcc653faeacb46c7e7c1f71e61663
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# shc

Generic shell script compiler.
More information: <https://manned.org/shc>.

- Compile a shell script:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>

- Compile a shell script and specify an output binary file:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary</span>

- Compile a shell script and set an expiration date for the executable:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dd/mm/yyyy</span>

- Compile a shell script and set a message to display upon expiration:

`shc -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dd/mm/yyyy</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Please contact your provider</span>`"`
