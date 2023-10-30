---
layout: page
title: common/acme.sh-dns (বাংলা)
description: "TLS সার্টিফিকেট ইস্যু করার জন্য DNS-01 চ্যালেঞ্জ ব্যবহার করুন।"
content_hash: 0a6998c7fcdc83ba72b6323ff4bb1e812271985f
last_modified_at: 2023-10-30
related_topics:
  - title: English version
    url: /en/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acme.sh-dns.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># acme.sh --dns

TLS সার্টিফিকেট ইস্যু করার জন্য DNS-01 চ্যালেঞ্জ ব্যবহার করুন।
আরও তথ্য পেতে: <https://github.com/acmesh-official/acme.sh/wiki>.

- স্বয়ংক্রিয় DNS API মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnd_gd</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- স্বয়ংক্রিয় DNS API মোড ব্যবহার করে একটি উইল্ডকার্ড সার্টিফিকেট (যা একটি পূর্বনির্দেশিত চিহ্ন (*) দ্বারা চিহ্নিত) ইস্যু করুন:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namesilo</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- DNS অ্যালিয়াস মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --challenge-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias-for-example-validation.com</span>

- DNS রেকর্ড যোগ করার পর স্বয়ংক্রিয় Cloudflare/Google DNS পোলিং বন্ধ করে একটি সার্টিফিকেট ইস্যু করুন, সেকেন্ডে নির্দিষ্ট কাস্টম প্রতীক্ষার সময় স্পেসিফাই করে:

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namecheap</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --dnssleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- ম্যানুয়াল DNS মোড ব্যবহার করে একটি সার্টিফিকেট ইস্যু করুন:

`acme.sh --issue --dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --yes-I-know-dns-manual-mode-enough-go-ahead-please`
