---
layout: page
title: common/magick-compare (हिन्दी)
description: "2 छवियों के बीच अंतर देखें।"
content_hash: 6425f3007ffc98a68fb59015049d49006160e794
last_modified_at: 2024-06-05
related_topics:
  - title: Deutsch version
    url: /de/common/magick-compare.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-compare.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/magick-compare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick compare

2 छवियों के बीच अंतर देखें।
अधिक जानकारी: <https://imagemagick.org/script/compare.php>।

- 2 छवियों की तुलना करें:

`magick compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अंतर.png</span>

- कस्टम मीट्रिक का उपयोग करके 2 छवियों की तुलना करें:

`magick compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अंतर.png</span>
