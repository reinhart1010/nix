---
layout: page
title: common/shasum (English)
description: "Calculate or check cryptographic SHA checksums."
content_hash: cf3e5cd889776dfd4cc6ce98e2155040bd5bae8e
last_modified_at: 2022-12-04
related_topics:
  - title: தமிழ் version
    url: /ta/common/shasum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/shasum.html
    icon: bi bi-globe
---
# shasum

Calculate or check cryptographic SHA checksums.
More information: <https://manned.org/shasum>.

- Calculate the SHA1 checksum for a file:

`shasum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate the SHA256 checksum for a file:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate the SHA512 checksum for multiple files:

`shasum --algorithm 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Calculate and save the list of SHA256 checksums to a file:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Check a file with a list of sums against the directory's files:

`shasum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check a list of sums and only show a message for files for which verification fails:

`shasum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Calculate the SHA1 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some_command</span>` | shasum`
