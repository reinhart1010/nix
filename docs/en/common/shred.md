---
layout: page
title: common/shred (English)
description: "Overwrite files to securely delete data."
content_hash: b9c281c284873cc4a636e598b0cf3a8560f394aa
last_modified_at: 2023-12-31
tldri18n_status: 2
---
# shred

Overwrite files to securely delete data.
More information: <https://www.gnu.org/software/coreutils/shred>.

- Overwrite a file:

`shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file and show progress on the screen:

`shred --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file, leaving [z]eros instead of random data:

`shred --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file a specific [n]umber of times:

`shred --iterations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file and remove it:

`shred --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Overwrite a file 100 times, add a final overwrite with [z]eros, remove the file after overwriting it and show [v]erbose progress on the screen:

`shred -vzun 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
