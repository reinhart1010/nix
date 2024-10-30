---
layout: page
title: windows/del (العربية)
description: "حذف ملف واحد او مجموعه من الملفات."
content_hash: 2e7c41953da7df9c1a50cde6ee83258ca33c04af
last_modified_at: 2024-10-30
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/del.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># del

حذف ملف واحد او مجموعه من الملفات.
وهو الاسم المستعار للامر `Remove-Item`.
هذه الوثائق تستند إلى إصدار سطر الأوامر (`cmd`) من `del`.
لمزيد من التفاصيل: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- اعرض التوثيقات للأمر الأصلي:

`tldr remove-item`

- حذف ملف او أكثر او حذف التطابق مع أنماط:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern1 file_pattern2 ...</span>

- التأكيد قبل الحذف:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /p`

- حذف ملفات القراءة فقط:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /f`

- حذف الملفات الموجودة في المجلد الحالي وأيضًا الملفات الفرعية:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /s`

- لا تطلب التأكيد عند حذف الملفات بناءً على محدد عام:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /q`

- عرض المساعدة وقائمة السمات المتاحة:

`del /?`

- حذف ملف اعتمادا على محدد معين:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute</span>
