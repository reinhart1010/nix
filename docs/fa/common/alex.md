---
layout: page
title: common/alex (فارسی)
description: "نوشته های نادرست و مشکل دار پیدا کنید."
content_hash: 48f1db4280fae01fc9358963b07c9619348a2bd4
last_modified_at: 2024-07-23
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/alex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># alex

نوشته های نادرست و مشکل دار پیدا کنید.
به شما کمک می کند نوشته های حاوی تعصب جنسیتی، دوقطبی کننده جامعه، نژاد پرستانه، توهین به مذاهب و سایر جملات مشابه را پیدا کنید.
اطلاعات بیشتر: <https://github.com/get-alex/alex>.

- بررسی کردن متن ورودی از `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- بررسی تمام فایل های موجود در این دایرکتوری:

`alex`

- بررسی یک فایل خاص:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.md</span>

- بررسی تمام فایل های نشانه گذاری به جز `example.md`:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.md</span>
