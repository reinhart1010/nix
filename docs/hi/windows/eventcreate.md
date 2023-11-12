---
layout: page
title: windows/eventcreate (हिन्दी)
description: "इवेंट लॉग में कस्टम प्रविष्टियाँ बनाएँ।"
content_hash: 3c6faac2e4eb75462dd5391ec0f560f3df67bfcc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/eventcreate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/eventcreate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eventcreate

इवेंट लॉग में कस्टम प्रविष्टियाँ बनाएँ।
इवेंट आईडी 1 और 1000 के बीच कोई भी संख्या हो सकती है।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/eventcreate>।

- लॉग में दी गई आईडी (1-1000) के साथ एक नया ईवेंट बनाएं:

`eventcreate /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">success|error|warning|information</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आईडी</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संदेश</span>`"`

- किसी विशिष्ट इवेंट लॉग में एक इवेंट बनाएं:

`eventcreate /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लॉग_नाम</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रकार</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आईडी</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संदेश</span>`"`

- किसी विशिष्ट स्रोत के साथ एक ईवेंट बनाएं:

`eventcreate /so `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_नाम</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रकार</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आईडी</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संदेश</span>`"`

- रिमोट मशीन के इवेंट लॉग में एक इवेंट बनाएं:

`eventcreate /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होस्ट का नाम</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता नाम</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पासवर्ड</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रकार</span>` /id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आईडी</span>` /d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संदेश</span>`"`
