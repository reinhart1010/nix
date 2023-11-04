---
layout: page
title: common/acme.sh (বাংলা)
description: "ACME ক্লায়েন্ট প্রোটোকল প্রয়োজনীয় স্ক্রিপ্ট, certbot এর একটি বিকল্প।"
content_hash: 4d99209c04ad3f33bae59f467f927f7e3abd078c
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/acme.sh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acme.sh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/acme.sh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh.html
    icon: bi bi-globe
---
# acme.sh

ACME ক্লায়েন্ট প্রোটোকল প্রয়োজনীয় স্ক্রিপ্ট, certbot এর একটি বিকল্প।
`acme.sh dns` দেখুন।
আরও তথ্য পেতে: <https://github.com/acmesh-official/acme.sh>.

- ওয়েবরুট মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --webroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/পাথ/টু/ওয়েবরুট</span>

- পোর্ট ৮০ ব্যবহার করে স্ট্যান্ডঅলোন মোড ব্যবহার করে একটি মাল্টিপল ডোমেনের জন্য একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --standalone --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- পোর্ট ৪৪৩ ব্যবহার করে স্ট্যান্ডঅলোন TLS মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --alpn --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- কাজকর্ম Nginx কনফিগারেশন ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- কাজকর্ম অ্যাপাচি কনফিগারেশন ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- স্বয়ংক্রিয় DNS API মোড ব্যবহার করে একটি উইল্ডকার্ড (\*) সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- নির্দিষ্ট অবস্থানে সার্টিফিকেট ফাইল ইনস্টল করুন (স্বয়ংক্রিয় সার্টিফিকেট পুনরারম্ভের জন্য উপযুক্ত):

`acme.sh --install-cert -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/পথ/থেকে/উদাহরণ.কম.কি</span>` --fullchain-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/পথ/থেকে/উদাহরণ.কম.সিআর</span>` --reloadcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"systemctl force-reload nginx"</span>
