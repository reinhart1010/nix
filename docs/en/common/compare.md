---
layout: page
title: common/compare (English)
description: "Create a comparison image to visually annotate the difference between two images."
content_hash: ffd78e7a8fcc375c9ca50665f2a606c48cd421d8
last_modified_at: 2023-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/compare.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/compare.html
    icon: bi bi-globe
---
# compare

Create a comparison image to visually annotate the difference between two images.
Part of ImageMagick.
More information: <https://imagemagick.org/script/compare.php>.

- Compare two images:

`compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>

- Compare two images using the specified metric:

`compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>
