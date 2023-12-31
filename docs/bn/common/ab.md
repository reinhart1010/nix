---
layout: page
title: common/ab (বাংলা)
description: "এপাচি এইচটিটিপি সার্ভার বেঞ্চমার্কিং টুল।"
content_hash: ab8edd11d9a2211f329975aeb8507cd7b03678fc
last_modified_at: 2023-12-31
related_topics:
  - title: Deutsch version
    url: /de/common/ab.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ab.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ab.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ab.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ab.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ab.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ab.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ab.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ab.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ab.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ab

এপাচি এইচটিটিপি সার্ভার বেঞ্চমার্কিং টুল।
আরও তথ্য পাবেন: <https://httpd.apache.org/docs/current/programs/ab.html>।

- নির্দিষ্ট URL এ ১০০টি HTTP GET অনুরোধ প্রয়ান করুন:

`ab -n 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- URL এ ১০০টি HTTP GET অনুরোধ, ১০টি সময়সার ব্যাচে একে অপরের পরে প্রয়ান করুন:

`ab -n 100 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">১০</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- URL এ ১০০টি HTTP POST অনুরোধ প্রয়ান করুন, একটি JSON পেলোড ব্যবহার করে:

`ab -n 100 -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application/json</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/ফাইল.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- HTTP [K]eep Alive ব্যবহার করুন, অর্থাৎ একটি HTTP সেশনে মাধ্যমে একাধিক অনুরোধ প্রয়ান করুন:

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- বেঞ্চমার্কিং করার জন্য সময় নির্ধারণ করার জন্য সর্বাধিক সেকেন্ড নির্ধারণ করুন:

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">৬০</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
