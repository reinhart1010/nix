---
layout: page
title: common/truncate (English)
description: "Shrink or extend the size of a file to the specified size."
content_hash: 063ad8188c6457a550bf26d609f1843763b60ddd
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# truncate

Shrink or extend the size of a file to the specified size.
More information: <https://www.gnu.org/software/coreutils/truncate>.

- Set a size of 10 GB to an existing file, or create a new file with the specified size:

`truncate --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Extend the file size by 50 MiB, fill with holes (which reads as zero bytes):

`truncate --size +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50M</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Shrink the file by 2 GiB, by removing data from the end of file:

`truncate --size -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2G</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Empty the file's content:

`truncate --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Empty the file's content, but do not create the file if it does not exist:

`truncate --no-create --size 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
