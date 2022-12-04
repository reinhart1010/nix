---
layout: page
title: common/shred (English)
description: "Overwrite files to securely delete data."
content_hash: d82bbea4555ed79c32778eba2ecd8d89b01f6a6f
last_modified_at: 2022-12-04
---
# shred

Overwrite files to securely delete data.
More information: <https://www.gnu.org/software/coreutils/shred>.

- Overwrite a file:

`shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file, leaving zeroes instead of random data:

`shred --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file 25 times:

`shred -n25 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file and remove it:

`shred --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
