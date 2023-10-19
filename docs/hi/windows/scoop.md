---
layout: page
title: windows/scoop (हिन्दी)
description: "स्कूप पैकेज मैनेजर।"
content_hash: 70bf4ab23ed180d94744c2e54edd626819d76efa
last_modified_at: 2023-10-19
related_topics:
  - title: Deutsch version
    url: /de/windows/scoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># scoop

स्कूप पैकेज मैनेजर।
अधिक जानकारी: <https://scoop.sh>.

- एक पैकेज स्थापित करें:

`scoop install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज निकालें:

`scoop uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- सभी स्थापित पैकेजों को अद्यतन करें:

`scoop update --all`

- स्थापित पैकेजों की सूची बनाएं:

`scoop list`

- किसी पैकेज के बारे में जानकारी प्रदर्शित करें:

`scoop info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज खोजें:

`scoop search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- सभी पैकेजों के पुराने संस्करण हटाएँ और डाउनलोड कैश साफ़ करें:

`scoop cleanup --cache --all`
