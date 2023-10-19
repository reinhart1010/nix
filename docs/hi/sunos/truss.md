---
layout: page
title: sunos/truss (हिन्दी)
description: "सिस्टम कॉल को ट्रेस करने के लिए समस्या निराकरण टूल।"
content_hash: d26c3d9fbede425532f654a78032ec03d883aba8
last_modified_at: 2023-10-19
related_topics:
  - title: English version
    url: /en/sunos/truss.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/truss.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/truss.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/truss.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/truss.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># truss

सिस्टम कॉल को ट्रेस करने के लिए समस्या निराकरण टूल।
SunOS का संगत strace।
अधिक जानकारी: <https://www.unix.com/man-page/linux/1/truss>.

- एक प्रोग्राम को ट्रेस करने के लिए प्रायोगिकरण करके उसकी सभी उपक्रमों का पालन करें:

`truss -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोग्राम</span>

- उसके PID द्वारा एक विशिष्ट प्रक्रिया को ट्रेस करने का प्रारंभ करें:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- एक प्रोग्राम को ट्रेस करने के लिए प्रायोगिकरण करके उसके आर्ग्यूमेंट और पर्यावरण परियोजना दिखाने का प्रारंभ करें:

`truss -a -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रोग्राम</span>

- प्रत्येक सिस्टम कॉल के लिए समय, कॉल्स, और त्रुटियों की गणना करें और प्रोग्राम बाहर निकलने पर एक संक्षेप रिपोर्ट करें:

`truss -c -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- सिस्टम कॉल के द्वारा आउटपुट को फ़िल्टर करते हुए एक प्रक्रिया को ट्रेस करें:

`truss -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सिस्टम_कॉल_नाम</span>
