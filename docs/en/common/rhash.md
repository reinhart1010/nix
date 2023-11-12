---
layout: page
title: common/rhash (English)
description: "Calculate or check common message digests."
content_hash: f0a6d5b0c20a70d040c7e2c8fb90285ccde105da
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rhash

Calculate or check common message digests.
More information: <https://rhash.sourceforge.net/manpage.php>.

- Calculate default CRC32 digests of a file:

`rhash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Recursively process a directory to generate an SFV file using SHA1:

`rhash --sha1 --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/folder</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.sfv</span>

- Verify the integrity of files based on an SFV file:

`rhash --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.sfv</span>

- Calculate the SHA3 digest of a text message:

`rhash --sha3-256 --message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`'`

- Calculate CRC32 digest of a file and output digest encoded in base64 using BSD format:

`rhash --base64 --bsd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use custom output template:

`rhash --printf '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%p\t%s\t%{mtime}\t%m\n</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
