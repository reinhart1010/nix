---
layout: page
title: windows/choco-upgrade (हिन्दी)
description: "चॉकलेटी के साथ एक या अधिक पैकेज अपग्रेड करें।"
content_hash: a4b1af4bbb274be3efbb8f14299ccd66794ff476
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-upgrade.html
    icon: bi bi-globe
---
# choco upgrade

चॉकलेटी के साथ एक या अधिक पैकेज अपग्रेड करें।
अधिक जानकारी: <https://chocolatey.org/docs/commands-upgrade>।

- एक या अधिक स्थान-पृथक पैकेजों को अपग्रेड करें:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज1 पैकेज2 ...</span>

- किसी पैकेज के विशिष्ट संस्करण में अपग्रेड करें:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">संस्करण</span>

- सभी पैकेज अपग्रेड करें:

`choco upgrade all`

- निर्दिष्ट अल्पविराम से अलग किए गए पैकेजों को छोड़कर सभी को अपग्रेड करें:

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज1 पैकेज2 ...</span>`"`

- सभी संकेतों की स्वचालित रूप से पुष्टि करें:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>` --yes`

- पैकेज प्राप्त करने के लिए एक कस्टम स्रोत निर्दिष्ट करें:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_यूआरएल|उपनाम</span>

- प्रमाणीकरण के लिए उपयोगकर्ता नाम और पासवर्ड प्रदान करें:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता नाम</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पासवर्ड</span>
