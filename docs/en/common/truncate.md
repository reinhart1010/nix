---
layout: page
title: common/truncate (English)
description: "Shrink or extend the size of a file to the specified size."
content_hash: 9491aa602590c0e59d22a91ab75f1cd62ad4e49a
last_modified_at: 2024-06-28
tldri18n_status: 2
---
# truncate

Shrink or extend the size of a file to the specified size.
More information: <https://www.gnu.org/software/coreutils/truncate>.

- Set a size of 10 GB to an existing file, or create a new file with the specified size:

`truncate --size 10G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Extend the file size by 50 MiB, fill with holes (which reads as zero bytes):

`truncate --size +50M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Shrink the file by 2 GiB, by removing data from the end of file:

`truncate --size -2G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Empty the file's content:

`truncate --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Empty the file's content, but do not create the file if it does not exist:

`truncate --no-create --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
