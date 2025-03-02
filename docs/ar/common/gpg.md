---
layout: page
title: common/gpg (العربية)
description: "برنامج GNU Privacy Guard."
content_hash: 8a95fc1738b9b1c06acd2609b148d1274cadbee9
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/gpg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/gpg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gpg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gpg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpg

برنامج GNU Privacy Guard.
راجع `gpg2` للحصول على الإصدار الثاني من GNU Privacy Guard. تقوم معظم أنظمة التشغيل بربط `gpg` بـ `gpg2`.
لمزيد من التفاصيل: <https://gnupg.org>.

- إنشاء مفتاح GPG عام وخاص بطريقة تفاعلية:

`gpg --full-generate-key`

- توقيع الملف `doc.txt` دون تشفير (يتم حفظ الإخراج في ملف `doc.txt.asc`):

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- تشفير وتوقيع الملف `doc.txt` للمستخدمين alice@example.com و bob@example.com (يتم حفظ الإخراج في ملف `doc.txt.gpg`):

`gpg --encrypt --sign --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bob@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- تشفير `doc.txt` باستخدام كلمة مرور فقط (يتم حفظ الإخراج في ملف `doc.txt.gpg`):

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- فك تشفير `doc.txt.gpg` (يتم عرض الإخراج على `stdout`):

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- استيراد مفتاح عام:

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.gpg</span>

- تصدير المفتاح العام للمستخدم alice@example.com (يتم عرض الإخراج على `stdout`):

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- تصدير المفتاح الخاص للمستخدم alice@example.com (يتم عرض الإخراج على `stdout`):

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
