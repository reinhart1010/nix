---
layout: page
title: common/shred (English)
description: "Overwrite files to securely delete data."
content_hash: 638e828dfcd869e5d81ddbe3ab7df1702f1612e8
---
# shred

Overwrite files to securely delete data.
More information: <https://www.gnu.org/software/coreutils/shred>.

- Overwrite a file:

`shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Overwrite a file, leaving zeroes instead of random data:

`shred --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Overwrite a file 25 times:

`shred -n25 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Overwrite a file and remove it:

`shred --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
