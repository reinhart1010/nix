---
layout: page
title: common/chmod (فارسی)
description: "تغییر مجوز(ها)ی دسترسی به یک فایل یا پوشه."
content_hash: 67c7ccc560211cfa9a28d8a18bcbe9098d091d38
last_modified_at: 2023-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chmod.html
    icon: bi bi-globe
---
# chmod

تغییر مجوز(ها)ی دسترسی به یک فایل یا پوشه.
اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/chmod>.

- به مالک فایل دسترسی اجرا میدهد:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل</span>

- به کابر مالک دسترسی خواند|نوشتن یک فایل|پوشه را میدهد:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل_یا_پوشه</span>

- دسترسی اجرا را از گروه صلب میکند:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل</span>

- به تمامی کاربرها دسترسی خواندن و اجرا میدهد:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل</span>

- به دیگران(کاربرانی که صاحب فایل نیستند) دسترسی های گروه را میدهد:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل</span>

- به همگان همه دسترسی(ها) را میدهد:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/فایل</span>

- به صورت بازگشتی به گروه و دیگران دسترسی نوشتن میدهد:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/پوشه</span>

- به صورت بازگشتی در پوشه و زیرپوشه(ها) دسترسی اجرا و خواندن فایل(ها) را میدهد:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسیر/به/پوشه</span>
