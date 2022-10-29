---
layout: page
title: common/tox (العربية)
description: "أتمتة اختبارات بايثون عبر إصدارات بايثون متعددة."
content_hash: 34415d55346f99d2e65b0441b891e6d7e5354f35
related_topics:
  - title: English version
    url: /en/common/tox.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tox

أتمتة اختبارات بايثون عبر إصدارات بايثون متعددة.
استخدم tox.ini لضبط البيئات وأمر الاختبار.
لمزيد من التفاصيل: <https://github.com/tox-dev/tox>.

- بدء الاختبارات على جميع بيئات الاختبار:

`tox`

- إنشاء ملف الإعدادات `tox.ini`:

`tox-quickstart`

- عرض قائمة جميع البيئات المتوفرة:

`tox --listenvs-all`

- بدء الاختبارات على بيئة معينة (مثال: بايثون 3.6):

`tox -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py36</span>

- إجبار إعادة إنشاء البيئة الافتراضية:

`tox --recreate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">py27</span>
