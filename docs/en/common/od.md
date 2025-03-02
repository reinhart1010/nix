---
layout: page
title: common/od (English)
description: "Display file contents in octal, decimal or hexadecimal format."
content_hash: b3bb52336a3f7fc8efb57d7a755bc25278abc3eb
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/od.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/od.html
    icon: bi bi-globe
tldri18n_status: 2
---
# od

Display file contents in octal, decimal or hexadecimal format.
Optionally display the byte offsets and/or printable representation for each line.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html>.

- Display file using default settings: octal format, 8 bytes per line, byte offsets in octal, and duplicate lines replaced with `*`:

`od `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display file in verbose mode, i.e. without replacing duplicate lines with `*`:

`od -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display file in hexadecimal format (2-byte units), with byte offsets in decimal format:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display file in hexadecimal format (1-byte units), and 4 bytes per line:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x1</span>` --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display file in hexadecimal format along with its character representation, and do not print byte offsets:

`od --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xz</span>` --address-radix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Read only 100 bytes of a file starting from the 500th byte:

`od --read-bytes 100 --skip-bytes=500 -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
