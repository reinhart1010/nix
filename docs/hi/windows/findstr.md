---
layout: page
title: windows/findstr (हिन्दी)
description: "एक या एक से अधिक फाइलों में निर्दिष्ट टेक्स्ट खोजें।"
content_hash: f1804cfcffb655547514fd47bd65d84049614f7a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/findstr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/findstr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# findstr

एक या एक से अधिक फाइलों में निर्दिष्ट टेक्स्ट खोजें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>।

- सभी फाइलों में एक या एक से अधिक स्ट्रिंग्स खोजें:

`findstr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्ट्रिंग1 स्ट्रिंग2 ...</span>`" *`

- एक पाईप्ड कमांड के आउटपुट में एक या एक से अधिक स्ट्रिंग्स खोजें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका</span>` | findstr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्ट्रिंग1 स्ट्रिंग2 ...</span>`"`

- सभी फाइलों में पुनरावृत्तिपूर्वक एक या एक से अधिक स्ट्रिंग्स खोजें:

`findstr /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्ट्रिंग1 स्ट्रिंग2 ...</span>`" *`

- केस-इंसेंसिटिव सर्च का उपयोग करके स्ट्रिंग्स खोजें:

`findstr /i "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्ट्रिंग1 स्ट्रिंग2 ...</span>`" *"`

- नियमित एक्सप्रेशंस का उपयोग करके सभी फाइलों में स्ट्रिंग्स खोजें:

`findstr /r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">एक्सप्रेशंस</span>`" *`

- सभी टेक्स्ट फाइलों में एक लिटरल स्ट्रिंग (जिसमें स्पेसेस शामिल हैं) खोजें:

`findstr /c:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्ट्रिंग1 स्ट्रिंग2 ...</span>`" *.txt`

- प्रत्येक मेल खाने वाली लाइन के पहले लाइन नंबर दिखाएं:

`findstr /n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्ट्रिंग1 स्ट्रिंग2 ...</span>`" *`

- केवल उन फाइलों के नाम दिखाएं जिनमें मैच पाया गया हो:

`findstr /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्ट्रिंग1 स्ट्रिंग2 ...</span>`" *`
