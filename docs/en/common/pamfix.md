---
layout: page
title: common/pamfix (English)
description: "Fix errors in PAM, PBM, PGM and PPM files."
content_hash: 01cb07996e93d210b9ca9afd0f670e54c0faca24
last_modified_at: 2024-06-03
tldri18n_status: 2
---
# pamfix

Fix errors in PAM, PBM, PGM and PPM files.
See also: `pamfile`, `pamvalidate`.
More information: <https://netpbm.sourceforge.net/doc/pamfix.html>.

- Fix a Netpbm file that is missing its last part:

`pamfix -truncate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/corrupted.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ext</span>

- Fix a Netpbm file where pixel values exceed the image's `maxval` by lowering the offending pixels' values:

`pamfix -clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/corrupted.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ext</span>

- Fix a Netpbm file where pixel values exceed the image's `maxval` by increasing it:

`pamfix -changemaxval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/corrupted.pam|pbm|pgm|ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam|pbm|pgm|ppm</span>
