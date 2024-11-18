---
layout: page
title: windows/choco-source (हिन्दी)
description: "चॉकलेटी वाले पैकेजों के लिए स्रोत प्रबंधित करें।"
content_hash: 55f43a14c1e915dc2f806ba4d961b011b1c24a76
last_modified_at: 2024-11-18
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-source.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-source.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/choco-source.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-source.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-source.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-source.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-source.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco source

चॉकलेटी वाले पैकेजों के लिए स्रोत प्रबंधित करें।
अधिक जानकारी: <https://chocolatey.org/docs/commands-source>।

- वर्तमान में उपलब्ध स्रोतों की सूची बनाएं:

`choco source list`

- एक नया पैकेज स्रोत जोड़ें:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">यूआरएल</span>

- क्रेडेंशियल्स के साथ एक नया पैकेज स्रोत जोड़ें:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">यूआरएल</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पासवर्ड</span>

- क्लाइंट प्रमाणपत्र के साथ एक नया पैकेज स्रोत जोड़ें:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">यूआरएल</span>` --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रमाणपत्र_फ़ाइल\का\पथ</span>

- पैकेज स्रोत सक्षम करें:

`choco source enable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>

- पैकेज स्रोत को अक्षम करें:

`choco source disable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>

- पैकेज स्रोत हटाएँ:

`choco source remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>
