---
layout: page
title: linux/apt-get (العربية)
description: "أداة إدارة الحزم لديبيان وأوبونتو."
content_hash: e217c8b3df8545cc24ec41fbcdd48c8ede43f471
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

أداة إدارة الحزم لديبيان وأوبونتو.
ابحث عن الحزم باستخدام `apt-cache`.
لمزيد من التفاصيل: <https://manned.org/apt-get.8>.

- تحديث قائمة الحزم الموجودة وإصداراتها (يوصى بتشغيله قبل أي أمر `apt-get` آخر):

`apt-get update`

- تثبيت حزمة معينة، أو تحديثها إلى آخر إصدار متوفر:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- إزالة حزمة معينة:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- إزالة حزمة معينة وملفات الإعدادات الخاصة بها:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- تطوير جميع الحزم المثبتة إلى أجدد الإصدارات المتوفرة:

`apt-get upgrade`

- تنظيف المستودع المحلي - إزالة ملفات الحزم (.deb) من التنزيلات المعطلة التي لم يعد من الممكن تنزيلها:

`apt-get autoclean`

- إزالة جميع الحزم التي لم تعد مطلوبة:

`apt-get autoremove`

- تطوير الحزم المثبتة (مثل `upgrade`)، ولكن تقوم بإزالة الحزم القديمة وتثبيت حزم إضافية لتلبية التوابع الجديدة:

`apt-get dist-upgrade`
