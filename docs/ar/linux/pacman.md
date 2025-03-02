---
layout: page
title: linux/pacman (العربية)
description: "أداة مدير الحزم لنظام Arch Linux."
content_hash: 35b6a23fe235c7cf7326c8d2b241de2fa32f5efd
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacman.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pacman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

أداة مدير الحزم لنظام Arch Linux.
انظر أيضًا: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
لأوامر مكافئة في مديري الحزم الآخرين، انظر <https://wiki.archlinux.org/title/Pacman/Rosetta>.
لمزيد من التفاصيل: <https://manned.org/pacman.8>.

- مزامنة وتحديث جميع الحزم:

`sudo pacman -Syu`

- تثبيت حزمة جديدة:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- إزالة حزمة والتبعيات الخاصة بها:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- البحث في قاعدة بيانات الحزم عن تعبير نمطي (Regular Expresssion) أو كلمة مفتاحية:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`

- البحث في قاعدة البيانات عن الحزم التي تحتوي على ملف محدد:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>`"`

- عرض الحزم المثبتة بشكل صريح (تم تثبيتها يدويًا بواسطة المستخدم) مع إصداراتها:

`pacman -Qe`

- عرض الحزم اليتيمة (المثبتة كـ تبعيات ولكنها غير مطلوبة من قبل أي حزمة):

`pacman -Qtdq`

- تفريغ ذاكرة التخزين المؤقت بالكامل لـ `pacman`:

`sudo pacman -Scc`
