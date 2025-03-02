---
layout: page
title: common/go (العربية)
description: "إدارة كود مصدر Go."
content_hash: aecab7014f77e192ae26cdce9b65dc0a6496cf23
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/go.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/go.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/go.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go

إدارة كود مصدر Go.
بعض الأوامر الفرعية مثل `build` تحتوي على توثيق استخدام خاص بها.
لمزيد من التفاصيل: <https://golang.org>.

- تنزيل وتثبيت حزمة محددة بالمسار الخاص بها:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_path</span>

- ترجمة وتشغيل ملف مصدر (يجب أن يحتوي على حزمة `main`):

`go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.go`

- ترجمة ملف مصدر إلى ملف تنفيذي باسم محدد:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.go`

- ترجمة الحزمة الموجودة في المجلد الحالي:

`go build`

- تنفيذ جميع اختبارات الحزمة الحالية (يجب أن تنتهي الملفات بـ `_test.go`):

`go test`

- ترجمة وتثبيت الحزمة الحالية:

`go install`

- تهيئة وحدة جديدة في المجلد الحالي:

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>
