---
layout: page
title: linux/rm (العربية)
description: "يستخدم الأمر لحذف الملفات او المجلدات"
content_hash: 4ee048f7333143c3f7feaa543398a0c5b78757bd
last_modified_at: 2025-03-02
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
tldri18n_status: 2
---
# rm

يستخدم الأمر لحذف الملفات او المجلدات
أنظر أيضًا: `rmdir`.
لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- حذف ملفات محددة:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- حذف ملفات محددة وتجاهل الملفات الغير موجودة:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- حذف ملفات محددة مع واجهة تفاعلية قبل اي حذف للتأكد:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- حذف ملفات محددة مع عرض تفاصيل حول كل عملية حذف:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- حذف ملفات ومجلدات محددة بشكل تسلسلي:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- حذف المجلدات الفارغة (هذه الطريقة تعتبر آمنة):

`rm --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
