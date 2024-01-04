---
layout: page
title: linux/apk (فارسی)
description: "ابزار مدیریت بسته آلپاین لینوکس."
content_hash: 3f39364afd46d8a00189c32ed7bc2ed7696a5c90
last_modified_at: 2024-01-04
related_topics:
  - title: Deutsch version
    url: /de/linux/apk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apk.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apk

ابزار مدیریت بسته آلپاین لینوکس.
اطلاعات بیشتر: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- آپدیت فهرست مخزن ها از تمام مخازن ریموت:

`apk update`

- نصب یک بسته جدید:

`apk add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- حذف یک بسته:

`apk del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- تعمیر یک بسته یا ارتقا آن بدون تغییر دادن وابستگی های اصلی:

`apk fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- جستجوی یک بسته با کلمات کلیدی:

`apk search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keywords</span>

- نمایش اطلاعات درمورد بسته مورد نظر:

`apk info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
