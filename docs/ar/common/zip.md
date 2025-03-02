---
layout: page
title: common/zip (العربية)
description: "أداة لضغط وحزم الملفات في أرشيف Zip."
content_hash: 649045a8ed78161b701b7c007120de5bde2812af
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/zip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zip.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/zip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zip.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/zip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip

أداة لضغط وحزم الملفات في أرشيف Zip.
انظر أيضًا: `unzip`.
لمزيد من التفاصيل: <https://manned.org/zip>.

- إضافة ملفات/مجلدات إلى أرشيف محدد ([r]بشكل متكرر):

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- إزالة ملفات/مجلدات من أرشيف محدد ([d]حذف):

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- أرشفة ملفات/مجلدات مع [x]استثناء عناصر معينة:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/excluded_files_or_directories</span>

- أرشفة ملفات/مجلدات مع مستوى ضغط محدد (`0` - الأقل، `9` - الأعلى):

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- إنشاء أرشيف [e]مشفر باستخدام كلمة مرور محددة:

`zip -r -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- أرشفة ملفات/مجلدات في أرشيف Zip مقسم[s] إلى أجزاء متعددة (مثل أجزاء بحجم 3 جيجابايت):

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- طباعة محتويات أرشيف محدد:

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/compressed.zip</span>
