---
layout: page
title: common/steamcmd (हिन्दी)
description: "स्टीम क्लाइंट का एक कमांड-लाइन संस्करण।"
content_hash: 596ae1be8f34a335abb85ac6260d041d8e23da87
last_modified_at: 2024-11-18
related_topics:
  - title: Deutsch version
    url: /de/common/steamcmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/steamcmd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/steamcmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# steamcmd

स्टीम क्लाइंट का एक कमांड-लाइन संस्करण।
अधिक जानकारी: <https://manned.org/steamcmd>।

- एक एप्लिकेशन को गुमनाम रूप से स्थापित या अपडेट करें:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">गुमनाम</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप आईडी</span>` +quit`

- निर्दिष्ट क्रेडेंशियल का उपयोग करके एक एप्लिकेशन को स्थापित या अपडेट करें:

`steamcmd +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप आईडी</span>` +quit`

- एक विशिष्ट प्लेटफॉर्म के लिए एक एप्लिकेशन स्थापित करें:

`steamcmd +@sSteamCmdForcePlatformType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows</span>` +login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">गुमनाम</span>` +app_update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ऐप आईडी</span>` validate +quit`
