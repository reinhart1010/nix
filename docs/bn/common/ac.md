---
layout: page
title: common/ac (বাংলা)
description: "ব্যবহারকারী কতক্ষণ সংযোগিত আছেন, সেই পরিস্থিতিগুলি প্রিন্ট করুন।"
content_hash: 37627b8fcbe893a12c0fd2c3b821d03e06958f48
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ac.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ac.html
    icon: bi bi-globe
---
# ac

ব্যবহারকারী কতক্ষণ সংযোগিত আছেন, সেই পরিস্থিতিগুলি প্রিন্ট করুন।
আরও জানতে: <https://man.openbsd.org/ac>.

- বর্তমান ব্যবহারকারী কত সময় ধরে সংযোগিত আছে, ঘণ্টায়:

`ac`

- ব্যবহারকারী কত সময় ধরে সংযোগিত আছে, এটি ঘণ্টায় প্রিন্ট করুন:

`ac -p`

- একজন বিশেষ ব্যবহারকারী কত সময় ধরে সংযোগিত আছে তা প্রিন্ট করুন:

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ব্যবহারকারী_নাম</span>

- একজন বিশেষ ব্যবহারকারী কত সময় ধরে সংযোগিত আছে তা প্রতি দিন ঘণ্টায় প্রিন্ট করুন (মোটও সহ):

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ব্যবহারকারী_নাম</span>
