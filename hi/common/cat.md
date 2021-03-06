---
layout: page
title: common/cat (हिन्दी)
description: "फ़ाइलों को प्रिंट और संक्षिप्त करें।"
content_hash: 6eb68d155ad270b4a71e70c36f8f8d78a9695222
related_topics:
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cat.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
---
# cat

फ़ाइलों को प्रिंट और संक्षिप्त करें।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/cat>।

- मानक आउटपुट में फ़ाइल की सामग्री प्रिंट करें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल</span>

- लक्ष्य फ़ाइल में कई फ़ाइलों को संयुक्त करें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_फ़ाइल</span>

- लक्ष्य फ़ाइल के अंत में कई फ़ाइलें संलग्न करें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लक्ष्य_फ़ाइल</span>

- सभी आउटपुट लाइनों की संख्या:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल</span>

- गैर-मुद्रण योग्य और सफेदस्थान पात्र प्रदर्शित करें (M-उपसर्ग के साथ यदि गैर-ASCII):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल</span>
