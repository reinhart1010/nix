---
layout: page
title: linux/aa-disable (বাংলা)
description: "অ্যাপআরমার এর নিরাপত্তা পলিসি নিষ্ক্রিয় করুন।"
content_hash: 946a764c0eb18ecb04bddd67a36b36b21d63f62b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/aa-disable.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aa-disable.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/aa-disable.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-disable.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aa-disable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-disable

অ্যাপআরমার এর নিরাপত্তা পলিসি নিষ্ক্রিয় করুন।
আরও দেখুন: `aa-complain`, `aa-enforce`, `aa-status`।
আরও তথ্য পাবেন: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>।

- প্রোফাইল নিষ্ক্রিয় করুন:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/প্রোফাইল১ পাথ/টু/প্রোফাইল২ ...</span>

- একটি ডিরেক্টরিতে প্রোফাইল নিষ্ক্রিয় করুন (সাধারণত `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">পাথ/টু/প্রোফাইলগুচ্ছ</span>
