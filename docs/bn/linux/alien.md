---
layout: page
title: linux/alien (বাংলা)
description: "ভিন্ন ইন্সটলেশন প্যাকেজকে অন্য বিন্যাস এ রূপান্তর।"
content_hash: d810fb29b7da5e5bdcea98998a1f111bcbf5dfe9
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/alien.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/alien.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alien

ভিন্ন ইন্সটলেশন প্যাকেজকে অন্য বিন্যাস এ রূপান্তর।
এছাড়াও দেখুন: 'debtap`, `.deb` কে আর্চ লিনাক্স এ রূপান্তর এর জন্য।
আরও তথ্য পাবেন: <https://manned.org/alien>।

- একটি নির্দিষ্ট ইন্সটলেশন ফাইলকে ডেবিয়ান বিন্যাসে রূপান্তর করুন ('.deb' এক্সটেনশন):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/ফাইল</span>

- একটি নির্দিষ্ট ইন্সটলেশন ফাইলকে রেড হ্যাট বিন্যাসে রূপান্তর করুন ('.rpm' এক্সটেনশন):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/ফাইল</span>

- একটি নির্দিষ্ট ইন্সটলেশন ফাইলকে স্লেকওয়ার ইন্সটলেশন ফাইলে রূপান্তর করুন ('.tgz' এক্সটেনশন):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/ফাইল</span>

- একটি নির্দিষ্ট ইন্সটলেশন ফাইলকে ডেবিয়ান বিন্যাসে রূপান্তর ও সিস্টেম এ ইন্সটল করুন:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/ফাইল</span>
