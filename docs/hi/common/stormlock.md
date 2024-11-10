---
layout: page
title: common/stormlock (हिन्दी)
description: "केंद्रीकृत लॉकिंग सिस्टम।"
content_hash: 5370a667019d6cf5bd1a6c3c01f437ffd9e9a2dc
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stormlock.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stormlock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Stormlock

केंद्रीकृत लॉकिंग सिस्टम।
अधिक जानकारी: <https://github.com/tmccombs/stormlock>।

- संसाधन के लिए लीज़ प्राप्त करें:

`stormlock acquire `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संसाधन</span>

- दिए गए संसाधन के लिए दी गई लीज़ को जारी करें:

`stormlock release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संसाधन</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लीज़_आईडी</span>

- किसी संसाधन के लिए वर्तमान लीज़ की जानकारी दिखाएं, यदि कोई हो:

`stormlock current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संसाधन</span>

- जांचें कि दिए गए संसाधन के लिए लीज़ वर्तमान में सक्रिय है या नहीं:

`stormlock is-held `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संसाधन</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लीज़_आईडी</span>
