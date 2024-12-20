---
layout: page
title: windows/certutil (हिन्दी)
description: "सर्टीफिकेट सूचना को प्रबंधित और विन्यसित करने के लिए एक टूल।"
content_hash: 651a4777e2867bbaa0bd8d6d611435883412b804
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/windows/certutil.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/certutil.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/certutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certutil

सर्टीफिकेट सूचना को प्रबंधित और विन्यसित करने के लिए एक टूल।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>।

- विन्यास सूचना या फ़ाइलों को डंप करें:

`certutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल_नाम</span>

- एक फ़ाइल को हेक्साडेसिमल में एनकोड करें:

`certutil -encodehex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फ़ाइल\का\पथ</span>

- एक फ़ाइल को बेस64 में एनकोड करें:

`certutil -encode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फ़ाइल\का\पथ</span>

- बेस64-एनकोड फ़ाइल को डीकोड करें:

`certutil -decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फ़ाइल\का\पथ</span>

- एक फ़ाइल पर एक आपातकालिक हैश उत्पन्न करें और प्रदर्शित करें:

`certutil -hashfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md2|md4|md5|sha1|sha256|sha384|sha512</span>
