---
layout: page
title: common/sha256sum (English)
description: "Calculate SHA256 cryptographic checksums."
content_hash: 8a657664e167b31b63232c6a3cf71a91199fa31b
last_modified_at: 2024-11-18
related_topics:
  - title: 한국어 version
    url: /ko/common/sha256sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sha256sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha256sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha256sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sha256sum

Calculate SHA256 cryptographic checksums.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calculate the SHA256 checksum for one or more files:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Calculate and save the list of SHA256 checksums to a file:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Calculate a SHA256 checksum from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sha256sum`

- Read a file of SHA256 sums and filenames and verify all files have matching checksums:

`sha256sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Only show a message for missing files or when verification fails:

`sha256sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Only show a message when verification fails, ignoring missing files:

`sha256sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sha256</span>

- Check known SHA256 sum of a file:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">known-sha256-sum-of-the-file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | sha256sum --check`
