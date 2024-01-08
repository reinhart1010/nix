---
layout: page
title: common/composer (فارسی)
description: "ابزاری بسته محور برای مدیریت وابستگی های پروژه های php."
content_hash: baafe82be1f7c92b1c898409bb66425c456de4c0
last_modified_at: 2024-01-08
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/composer.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/composer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/composer.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/composer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# composer

ابزاری بسته محور برای مدیریت وابستگی های پروژه های php.
اطلاعات بیشتر: <https://getcomposer.org/>.

- ساخت یک فایل `composer.json` به صورت کنشگرا:

`composer init`

- اضافه کردن یک بسته به عنوان وابستگی به این پروژه، همچنین یک ورودی به `composer.json` وارد می کند:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package</span>

- نصب تمام وابستگی های این پروژه که در `composer.json` هستند و `composer.lock` را ایجاد می کند:

`composer install`

- حذف یک بسته از این پروژه، وابستگی مربوط به آنرا از `composer.json` و `composer.lock` حذف می کند:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package</span>

- بروزرسانی تمام وابستگی های این پروژه که در `composer.json` هستند و یادداشت کردن نسخه های جدید در فایل `composer.lock`:

`composer update`

- فقط `composer.lock` را بروزرسانی می کند بعد از این که `composer.json` را به صورت دستی بروزرسانی کردید:

`composer update --lock`

- اطلاعات بیشتری درباره دلیل نصب نشدن یک وابستگی ارائه می دهد:

`composer why-not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package</span>

- بروزرسانی کامپوزر به آخرین نسخه اش:

`composer self-update`
