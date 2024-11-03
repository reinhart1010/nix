---
layout: page
title: freebsd/base64 (हिन्दी)
description: "फ़ाइल या `stdin` को base64 में एन्कोड या डिकोड करें, `stdout` या किसी अन्य फ़ाइल में।"
content_hash: b874e65f9660068f9ef23ced9a6140d5e7e54b63
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/freebsd/base64.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

फ़ाइल या `stdin` को base64 में एन्कोड या डिकोड करें, `stdout` या किसी अन्य फ़ाइल में।
अधिक जानकारी: <https://man.freebsd.org/cgi/man.cgi?query=base64>।

- फ़ाइल को `stdout` में एन्कोड करें:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/का/पथ</span>

- फ़ाइल को निर्दिष्ट आउटपुट फ़ाइल में एन्कोड करें:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इनपुट_फाइल/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फाइल/का/पथ</span>

- एन्कोडेड आउटपुट को एक विशेष चौड़ाई पर लपेटें (`0` लपेटने को अक्षम करता है):

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--break</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|76|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/का/पथ</span>

- फ़ाइल को `stdout` में डिकोड करें:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/का/पथ</span>

- `stdin` से `stdout` में एन्कोड करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | base64`

- `stdin` से `stdout` में डिकोड करें:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>
