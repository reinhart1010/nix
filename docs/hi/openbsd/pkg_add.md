---
layout: page
title: openbsd/pkg_add (हिन्दी)
description: "OpenBSD में पैकेज स्थापित/अपडेट करें।"
content_hash: 59c29acc35ab23bb34c7e1440d28b9906ac3335b
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/pkg_add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_add

OpenBSD में पैकेज स्थापित/अपडेट करें।
देखें: `pkg_info`, `pkg_delete`।
अधिक जानकारी: <https://man.openbsd.org/pkg_add>।

- सभी पैकेज अपडेट करें, जिसमें निर्भरताएँ शामिल हैं:

`pkg_add -u`

- एक नया पैकेज स्थापित करें:

`pkg_add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- `pkg_info` के कच्चे आउटपुट से पैकेज स्थापित करें:

`pkg_add -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पथ/से/फाइल</span>
