---
layout: page
title: windows/cmdkey (हिन्दी)
description: "संग्रहीत उपयोगकर्ता_नाम और पासवर्ड बनाएं, दिखाएं और हटाएं।"
content_hash: 60e6c387542e5d8b3fc2b838e59cc939af414a4a
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/windows/cmdkey.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/cmdkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmdkey

संग्रहीत उपयोगकर्ता_नाम और पासवर्ड बनाएं, दिखाएं और हटाएं।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>।

- सभी उपयोगकर्ता क्रेडेंशियल्स की एक सूची दिखाएं:

`cmdkey /list`

- सभी उपयोगकर्ता क्रेडेंशियल्स की एक सूची दिखाएं:

`cmdkey /add:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">सर्वर_का_नाम</span>` /user:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- किसी विशिष्ट लक्ष्य के लिए क्रेडेंशियल हटाएं:

`cmdkey /delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_नाम</span>
