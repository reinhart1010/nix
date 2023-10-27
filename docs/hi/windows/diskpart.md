---
layout: page
title: windows/diskpart (हिन्दी)
description: "डिस्क, वॉल्यूम और विभाजन प्रबंधक।"
content_hash: e9c790e458e47d9f5a08bc633aedfa586f019a08
last_modified_at: 2023-10-27
related_topics:
  - title: English version
    url: /en/windows/diskpart.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/diskpart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/diskpart.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># diskpart

डिस्क, वॉल्यूम और विभाजन प्रबंधक।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- इसकी कमांड-लाइन दर्ज करने के लिए प्रशासनिक कमांड प्रॉम्प्ट में डिस्कपार्ट (diskpart) को स्वयं चलाएँ:

`diskpart`

- सभी डिस्क की सूची बनाएं:

`list disk`

- एक वॉल्यूम चुनें:

`select volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">वॉल्यूम</span>

- चयनित वॉल्यूम के लिए एक ड्राइव अक्षर (letter) निर्दिष्ट करें:

`assign letter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अक्षर</span>

- एक नया विभाजन बनाएँ:

`create partition primary`

- चयनित वॉल्यूम सक्रिय करें:

`active`

- डिस्कपार्ट (diskpart) से बाहर निकलें:

`exit`
