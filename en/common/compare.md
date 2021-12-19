---
layout: page
title: common/compare (English)
description: "View the difference between 2 images."
content_hash: 1cff23b7e3c23c959285c7b957e885d3fd41a021
related_topics:
  - title: Deutsch version
    url: /de/common/compare.html
    icon: bi bi-globe
---
# compare

View the difference between 2 images.
More information: <https://imagemagick.org/script/compare.php>.

- Compare 2 images:

`compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.png</span>

- Compare 2 images using a custom metric:

`compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diff.png</span>
