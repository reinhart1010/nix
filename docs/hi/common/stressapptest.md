---
layout: page
title: common/stressapptest (हिन्दी)
description: "उपयोगकर्ता स्थान मेमोरी और IO परीक्षण।"
content_hash: 15ffc9120c06ac8ca062fcff741eafc0c6f5c107
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stressapptest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stressapptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stressapptest

उपयोगकर्ता स्थान मेमोरी और IO परीक्षण।
अधिक जानकारी: <https://github.com/stressapptest/stressapptest>।

- दिए गए मेमोरी (मेगाबाइट में) की मात्रा का परीक्षण करें:

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्मृति</span>

- दिए गए फ़ाइल के लिए मेमोरी और I/O दोनों का परीक्षण करें:

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्मृति</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- परीक्षण जो विस्तृत स्तर को निर्दिष्ट करता है, जहाँ 0=न्यूनतम, 20=अधिकतम, 8=डिफ़ॉल्ट:

`stressapptest -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्मृति</span>` -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्तर</span>
