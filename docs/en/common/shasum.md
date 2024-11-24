---
layout: page
title: common/shasum (English)
description: "Calculate SHA cryptographic checksums."
content_hash: d15ae2b43d67c8544075d339403d7099200c63fd
last_modified_at: 2024-11-24
related_topics:
  - title: 한국어 version
    url: /ko/common/shasum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/shasum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/shasum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shasum

Calculate SHA cryptographic checksums.
More information: <https://manned.org/shasum>.

- Calculate the SHA1 checksum for one or more files:

`shasum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate the SHA checksum for one or more files with the specified algorithm:

`shasum --algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|224|256|384|512|512224|512256</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate a SHA1 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | shasum`

- Calculate and save the list of SHA256 checksums to a file:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Read a file of SHA checksums and filenames and verify all files have matching checksums (the algorithm will be automatically detected):

`shasum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Only show a message for missing files or when verification fails:

`shasum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Only show a message when verification fails, ignoring missing files:

`shasum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check a known SHA checksum of a file:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">known_sha_checksum_of_the_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | shasum --check`
