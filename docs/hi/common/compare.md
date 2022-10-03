---
layout: page
title: common/compare (हिन्दी)
description: "2 छवियों के बीच अंतर देखें।"
content_hash: d833878edba0abe199e3ae2e8b1986fb184e6b91
related_topics:
  - title: Deutsch version
    url: /de/common/compare.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/compare.html
    icon: bi bi-globe
---
# compare

2 छवियों के बीच अंतर देखें।
अधिक जानकारी: <https://imagemagick.org/script/compare.php>।

- 2 छवियों की तुलना करें:

`compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अंतर.png</span>

- कस्टम मीट्रिक का उपयोग करके 2 छवियों की तुलना करें:

`compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अंतर.png</span>
