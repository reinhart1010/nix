---
layout: page
title: common/pamoil (English)
description: "Turn a PAM image into an oil painting."
content_hash: 3d727552e7f1d496700b24a88bafdcc357f83491
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pamoil

Turn a PAM image into an oil painting.
More information: <https://netpbm.sourceforge.net/doc/pamoil.html>.

- Turn a PAM image into an oil painting:

`pamoil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pam</span>

- Consider a neighborhood of N pixels for the "smearing" effect:

`pamoil -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pam</span>
