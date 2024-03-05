---
layout: page
title: common/pambrighten (English)
description: "Change a PAM image's saturation and value."
content_hash: f4e7bbc51b72e898df87e75b96064d6867c97533
last_modified_at: 2024-03-05
tldri18n_status: 2
---
# pambrighten

Change a PAM image's saturation and value.
More information: <https://netpbm.sourceforge.net/doc/pambrighten.html>.

- Increase the saturation of each pixel by the specified percentage:

`pambrighten -saturation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value_percent</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Increase the value (from the HSV color space) of each pixel by the specified percentage:

`pambrighten -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value_percent</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
