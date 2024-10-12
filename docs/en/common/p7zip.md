---
layout: page
title: common/p7zip (English)
description: "Wrapper of 7-Zip file archiver with high compression ratio."
content_hash: ee07845c7e6274d05dd8bcb95c7ad526423b69a2
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# p7zip

Wrapper of 7-Zip file archiver with high compression ratio.
Internally executes either 7za or 7zr command.
More information: <https://p7zip.sourceforge.net>.

- Archive a file, replacing it with a 7zipped compressed version:

`p7zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Archive a file keeping the input file:

`p7zip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Decompress a file, replacing it with the original uncompressed version:

`p7zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed.ext</span>`.7z`

- Decompress a file keeping the input file:

`p7zip -d -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compressed.ext</span>`.7z`

- Skip some checks and force compression or decompression:

`p7zip -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
