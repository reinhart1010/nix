---
layout: page
title: windows/cmdkey (हिन्दी)
description: "संग्रहीत उपयोगकर्ता नाम और पासवर्ड बनाएं, दिखाएं और हटाएं।"
content_hash: eb73173ea000585281fca280c3fc89e95d98873b
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/windows/cmdkey.html
    icon: bi bi-globe
---
# cmdkey

संग्रहीत उपयोगकर्ता नाम और पासवर्ड बनाएं, दिखाएं और हटाएं।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>।

- सभी उपयोगकर्ता क्रेडेंशियल्स की एक सूची दिखाएं:

`cmdkey /list`

- सभी उपयोगकर्ता क्रेडेंशियल्स की एक सूची दिखाएं:

`cmdkey /add:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सर्वर_का_नाम</span>` /user:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- किसी विशिष्ट लक्ष्य के लिए क्रेडेंशियल हटाएं:

`cmdkey /delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_नाम</span>
