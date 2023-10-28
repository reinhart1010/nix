---
layout: page
title: common/babel (हिन्दी)
description: "एक ट्रांसपिलर जो कोड को जावास्क्रिप्ट ES6/ES7 सिंटैक्स से ES5 सिंटैक्स में परिवर्तित करता है।"
content_hash: 7c52516d330d88277409ad78f8f9d54f7d121670
last_modified_at: 2023-10-28
related_topics:
  - title: English version
    url: /en/common/babel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/babel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/babel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/babel.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/babel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/babel.html
    icon: bi bi-globe
---
# babel

एक ट्रांसपिलर जो कोड को जावास्क्रिप्ट ES6/ES7 सिंटैक्स से ES5 सिंटैक्स में परिवर्तित करता है।
अधिक जानकारी: <https://babeljs.io/>.

- एक निर्दिष्ट इनपुट फ़ाइल और आउटपुट को `stdout` में ट्रांसपाइल करें:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक निर्दिष्ट इनपुट फ़ाइल और आउटपुट को `stdout` में ट्रांसपाइल करें:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल/का/पथ</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फाइल/का/पथ</span>

- हर बार बदले जाने पर इनपुट फ़ाइल को ट्रांसपाइल करें:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल/का/पथ</span>` --watch`

- फ़ाइलों की एक पूरी निर्देशिका ट्रांसपाइल करें:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_निर्देशिका/का/पथ</span>

- निर्देशिका में निर्दिष्ट अल्पविराम से अलग की गई फ़ाइलों को अनदेखा करें:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_निर्देशिका/का/पथ</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अनदेखा_फ़ाइलें</span>

- न्यूनतम जावास्क्रिप्ट के रूप में ट्रांसपाइल और आउटपुट:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल/का/पथ</span>` --minified`

- आउटपुट फ़ॉर्मेटिंग के लिए प्रीसेट का एक सेट चुनें:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फ़ाइल/का/पथ</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रीसेटस</span>

- सभी उपलब्ध विकल्पों को आउटपुट करें:

`babel --help`
