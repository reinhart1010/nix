---
layout: page
title: common/pamstack (English)
description: "Stack the planes of multiple PAM images into one PAM image."
content_hash: e39d10f4bdf551422f6cea567c364988c26a33d8
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# pamstack

Stack the planes of multiple PAM images into one PAM image.
More information: <https://netpbm.sourceforge.net/doc/pamstack.html>.

- Stack the planes of the specified PAM images in the specified order:

`pamstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.pam path/to/image2.pam ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Specify the tuple type name of the output PAM file (maximum of 255 characters):

`pamstack -tupletype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tuple_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.pam path/to/image2.pam ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
