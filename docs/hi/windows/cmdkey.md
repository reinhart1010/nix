---
layout: page
title: windows/cmdkey (हिन्दी)
description: "संग्रहीत उपयोगकर्ता नाम और पासवर्ड बनाएं, दिखाएं और हटाएं।"
content_hash: 2505bd1842a19d77fb86ec3048cbc007d566e539
last_modified_at: 2023-10-26
related_topics:
  - title: English version
    url: /en/windows/cmdkey.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmdkey

संग्रहीत उपयोगकर्ता नाम और पासवर्ड बनाएं, दिखाएं और हटाएं।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>.

- सभी उपयोगकर्ता क्रेडेंशियल्स की एक सूची दिखाएं:

`cmdkey /list`

- सभी उपयोगकर्ता क्रेडेंशियल्स की एक सूची दिखाएं:

`cmdkey /add:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सर्वर_का_नाम</span>` /user:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- किसी विशिष्ट लक्ष्य के लिए क्रेडेंशियल हटाएं:

`cmdkey /delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_नाम</span>
