---
layout: page
title: common/pamslice (English)
description: "Extract one line of values out of a PAM image."
content_hash: a477b88a1d8cfe10755df00301347afab35a0889
last_modified_at: 2024-03-05
tldri18n_status: 2
---
# pamslice

Extract one line of values out of a PAM image.
More information: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- Print the values of the pixels in the n'th row in a table:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>

- Print the values of the pixels in the n'th column in a table:

`pamslice -column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>

- Consider the m'th plane of the input image only:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -plane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>

- Produce output in a format suitable for input to an `xmgr` for visualisation:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -xmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>
