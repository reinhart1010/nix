---
layout: page
title: common/ftp (العربية)
description: "أدوات للتفاعل مع الخادم عبر بروتوكول نقل الملفات (FTP)."
content_hash: 18e5871cb58fa21edbd390da2afbe0916a8ec96a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ftp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ftp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ftp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ftp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

أدوات للتفاعل مع الخادم عبر بروتوكول نقل الملفات (FTP).
لمزيد من التفاصيل: <https://manned.org/ftp>.

- الاتصال بخادم FTP:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.example.com</span>

- الاتصال بخادم FTP مع تحديد عنوان الـ IP والمنفذ:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- التبديل إلى وضع النقل الثنائي (الرسوميات، الملفات المضغوطة، إلخ):

`binary`

- نقل عدة ملفات دون طلب تأكيد على كل ملف:

`prompt off`

- تنزيل عدة ملفات (تعليمات الكلمة العامة glob):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- رفع عدة ملفات (تعليمات الكلمة العامة glob):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- حذف عدة ملفات على الخادم:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- إعادة تسمية ملف على الخادم:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">original_filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_filename</span>
