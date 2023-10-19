---
layout: page
title: windows/date (हिन्दी)
description: "सिस्टम दिनांक प्रदर्शित या सेट करता है।"
content_hash: b3ed476ce480685fe35b1253d9a4d670ffb4472d
last_modified_at: 2023-10-19
related_topics:
  - title: English version
    url: /en/windows/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/date.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># date

सिस्टम दिनांक प्रदर्शित या सेट करता है।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/date>.

- वर्तमान सिस्टम तिथि प्रदर्शित करें और नई तिथि दर्ज करने का संकेत दें (अपरिवर्तित रखने के लिए खाली छोड़ें):

`date`

- नई तिथि का संकेत दिए बिना वर्तमान सिस्टम तिथि प्रदर्शित करें:

`date /t`

- वर्तमान सिस्टम दिनांक को किसी विशिष्ट दिनांक में बदलें:

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">दिन</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वर्ष</span>
