---
layout: page
title: windows/certutil (English)
description: "A tool to manage and configure certificate information."
content_hash: 1adf1d984478d8babf6c98807bfb94a94fde6318
last_modified_at: 2023-10-17
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># certutil

A tool to manage and configure certificate information.
More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil>.

- Dump the configuration information or files:

`certutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Encode a file in hexadecimal:

`certutil -encodehex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\output_file</span>

- Encode a file to Base64:

`certutil -encode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\output_file</span>

- Decode a Base64-encoded file:

`certutil -decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\output_file</span>

- Generate and display a cryptographic hash over a file:

`certutil -hashfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md2|md4|md5|sha1|sha256|sha384|sha512</span>
