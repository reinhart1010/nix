---
layout: page
title: common/stl2gts (हिन्दी)
description: "STL फ़ाइलों को GTS (GNU त्रिकोणित सतह पुस्तकालय) फ़ाइल प्रारूप में परिवर्तित करें।"
content_hash: 2b63fb105a1d2fb80552d36d50cc3cb222c7f7a4
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stl2gts.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stl2gts.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stl2gts

STL फ़ाइलों को GTS (GNU त्रिकोणित सतह पुस्तकालय) फ़ाइल प्रारूप में परिवर्तित करें।
अधिक जानकारी: <https://manned.org/stl2gts>।

- एक STL फ़ाइल को GTS फ़ाइल में परिवर्तित करें:

`stl2gts < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.stl/का/पथ</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.gts/का/पथ</span>

- एक STL फ़ाइल को GTS फ़ाइल में परिवर्तित करें और फेस नॉर्मल्स को उलटें:

`stl2gts --revert < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.stl/का/पथ</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.gts/का/पथ</span>

- एक STL फ़ाइल को GTS फ़ाइल में परिवर्तित करें और वर्टिस को मर्ज न करें:

`stl2gts --nomerge < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.stl/का/पथ</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.gts/का/पथ</span>

- एक STL फ़ाइल को GTS फ़ाइल में परिवर्तित करें और सतह के आँकड़े प्रदर्शित करें:

`stl2gts --verbose < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.stl/का/पथ</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल.gts/का/पथ</span>

- सहायता प्रदर्शित करें:

`stl2gts --help`
