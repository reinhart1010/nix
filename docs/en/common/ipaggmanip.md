---
layout: page
title: common/ipaggmanip (English)
description: "Manipulate aggregate statistics produced by `ipaggcreate`."
content_hash: 6c4dfb73b9334caabc182dba814de541013fca07
---
# ipaggmanip

Manipulate aggregate statistics produced by `ipaggcreate`.
More information: <https://manned.org/ipaggmanip>.

- Combine labels equal in their high-order bits:

`ipaggmanip --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove labels with a count smaller than a given number of bytes and output a random sample of such labels:

`ipaggmanip --cut-smaller `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --cull-labels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Replace each label's count with 1 if it is non-zero:

`ipaggmanip --posterize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
