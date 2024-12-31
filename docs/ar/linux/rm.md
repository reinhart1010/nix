---
layout: page
title: linux/rm (العربية)
description: "يستخدم الأمر لحذف الملفات او المجلدات"
content_hash: 42bc86c412146c4014557aa5a47e5d942b3ae8df
last_modified_at: 2024-12-31
related_topics:
  - title: English version
    url: /en/linux/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rm.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rm

يستخدم الأمر لحذف الملفات او المجلدات
أنظر أيضًا: `rmdir`.
لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/rm>.

- حذف ملفات محددة:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">المسار/إلى/الملف1 المسار/إلى/الملف2 ...</span>

- حذف ملفات محددة وتجاهل الملفات الغير موجودة:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">المسار/إلى/الملف1 المسار/إلى/الملف2 ...</span>

- حذف ملفات محددة مع واجهة تفاعلية قبل اي حذف للتأكد:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">المسار/إلى/الملف1 المسار/إلى/الملف2 ...</span>

- حذف ملفات محددة مع عرض تفاصيل حول كل عملية حذف:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">المسار/إلى/الملف1 المسار/إلى/الملف2 ...</span>

- حذف ملفات ومجلدات محددة بشكل تسلسلي:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">المسار/إلى/الملف_أو_المجلد1 المسار/إلى/الملف_أو_المجلد2 ...</span>

- حذف المجلدات الفارغة (هذه الطريقة تعتبر آمنة):

`rm --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">المسار/إلى/المجلد</span>
