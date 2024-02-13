---
layout: page
title: common/pamstretch (English)
description: "Scale up a PAM image by interpolating between pixels."
content_hash: 3ad4c9a24e3ed8530988edef1b29727411d68a22
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# pamstretch

Scale up a PAM image by interpolating between pixels.
See also: `pamstretch-gen`, `pamenlarge`, `pamscale`.
More information: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

- Scale up a PAM image by an integer factor:

`pamstretch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Scale up a PAM image by the specified factors in the horizontal and vertical directions:

`pamstretch -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
