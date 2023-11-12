---
layout: page
title: linux/apt (العربية)
description: "أداة إدارة الحزم للتوزيعات القائمة على ديبيان."
content_hash: 08f4974dabeed6e8de5f5a6c85e77f5b836881ba
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

أداة إدارة الحزم للتوزيعات القائمة على ديبيان.
بديل لـ `apt-get` عند الاستخدام الفعال في إصدارات أوبونتو 16.04 وما بعده.
لمزيد من التفاصيل: <https://manpages.debian.org/latest/apt/apt.8.html>.

- تحديث قائمة الحزم الموجودة وإصداراتها (يوصى بتشغيله قبل أي أمر `apt` آخر):

`sudo apt update`

- البحث عن حزمة معينة:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">الحزمة</span>

- إظهار معلومات حول حزمة معينة:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">الحزمة</span>

- تثبيت حزمة معينة، أو تحديثها إلى آخر إصدار متوفر:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">الحزمة</span>

- إزالة حزمة معينة (استخدام `purge` لحذف ملفات الإعدادات الخاصة بالحزمة):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">الحزمة</span>

- تطوير جميع الحزم المثبتة إلى أجدد الإصدارات المتوفرة:

`sudo apt upgrade`

- إظهار قائمة جميع الحزم:

`apt list`

- إظهار قائمة جميع الحزم المثبتة:

`apt list --installed`
