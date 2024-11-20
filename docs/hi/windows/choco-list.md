---
layout: page
title: windows/choco-list (हिन्दी)
description: "चॉकलेट के साथ पैकेजों की सूची प्रदर्शित करें।"
content_hash: d08b2c4c110cd697fcdf206f4e39680fe204cf5e
last_modified_at: 2024-11-20
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/choco-list.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/choco-list.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco list

चॉकलेट के साथ पैकेजों की सूची प्रदर्शित करें।
अधिक जानकारी: <https://chocolatey.org/docs/commands-list>।

- सभी उपलब्ध पैकेज प्रदर्शित करें:

`choco list`

- सभी स्थानीय रूप से स्थापित पैकेज प्रदर्शित करें:

`choco list --local-only`

- स्थानीय कार्यक्रमों सहित सूची प्रदर्शित करें:

`choco list --include-programs`

- केवल अनुमोदित पैकेज प्रदर्शित करें:

`choco list --approved-only`

- पैकेज प्रदर्शित करने के लिए एक कस्टम स्रोत निर्दिष्ट करें:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">स्रोत_URL|उपनाम</span>

- प्रमाणीकरण के लिए एक उपयोगकर्ता नाम और पासवर्ड प्रदान करें:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पासवर्ड</span>
