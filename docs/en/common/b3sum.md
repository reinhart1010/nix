---
layout: page
title: common/b3sum (English)
description: "Calculate BLAKE3 cryptographic checksums."
content_hash: ca30284ed82723fc87020f5634ce1a064d2c0003
last_modified_at: 2024-11-24
related_topics:
  - title: français version
    url: /fr/common/b3sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/b3sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b3sum

Calculate BLAKE3 cryptographic checksums.
More information: <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- Calculate the BLAKE3 checksum for one or more files:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of BLAKE3 checksums to a file:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>

- Calculate a BLAKE3 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | b3sum`

- Read a file of BLAKE3 checksums and filenames and verify all files have matching checksums:

`b3sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>

- Only show a message for missing files or when verification fails:

`b3sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.b3</span>

- Check a known BLAKE3 checksum of a file:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">known_blake3_checksum_of_the_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | b3sum --check`
