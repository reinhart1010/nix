---
layout: page
title: common/truncate (English)
description: "Shrink or extend the size of a file to the specified size."
content_hash: 89bb2512eb0791744a9780d1a2cd6bd1b274f3aa
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/truncate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/truncate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# truncate

Shrink or extend the size of a file to the specified size.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html>.

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
