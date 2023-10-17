---
layout: page
title: windows/winget (हिन्दी)
description: "विंडोज़ पैकेज प्रबंधक।"
content_hash: 551eec38240ad755a34f7766d281a22e5d6c45a3
last_modified_at: 2023-10-17
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/winget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
---
# winget

विंडोज़ पैकेज प्रबंधक।
अधिक जानकारी: <https://learn.microsoft.com/windows/package-manager/winget>.

- एक पैकेज इनस्टॉल करें:

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज निकालें (अनइंस्टॉल करें): (नोट: `uninstall` की जगह `remove` का भी इस्तेमाल किया जा सकता है):

`winget uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- पैकेज के बारे में जानकारी प्रदर्शित करें:

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- पैकेज की खोज करें:

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- सभी पैकेज़ को नवीनतम संस्करणों में अपग्रेड करें:

`winget upgrade --all`

- `winget` के साथ प्रबंधित इन्सटाल्ड पैकेजों की सूची बनाएं:

`winget list --source winget`

- किसी फ़ाइल से पैकेज आयात करें, या स्थापित पैकेज़ को किसी फ़ाइल में निर्यात करें:

`winget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import|export</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--import-file|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- विंगेट-पीकेजीएस(winget-pkgs) रिपॉजिटरी में पीआर(PR) सबमिट करने से पहले मैनिफ़ेस्ट को सत्यापित करें:

`winget validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रकट/का/पथ</span>
