---
layout: page
title: common/compare (हिन्दी)
description: "2 छवियों के बीच अंतर देखें।"
content_hash: d833878edba0abe199e3ae2e8b1986fb184e6b91
last_modified_at: 2024-06-04
related_topics:
  - title: Deutsch version
    url: /de/common/compare.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/compare.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/compare.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># compare

2 छवियों के बीच अंतर देखें।
अधिक जानकारी: <https://imagemagick.org/script/compare.php>।

- 2 छवियों की तुलना करें:

`compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अंतर.png</span>

- कस्टम मीट्रिक का उपयोग करके 2 छवियों की तुलना करें:

`compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">छवि2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अंतर.png</span>
