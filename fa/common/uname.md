---
layout: page
title: common/uname (فارسی)
description: "نمایش اطلاعاتی درباره سخت افزار و سیستم عامل."
content_hash: 588c76d8fae1c14e72a549ab2136c8fcab4175a8
related_topics:
  - title: English version
    url: /en/common/uname.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/uname.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/uname.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uname

نمایش اطلاعاتی درباره سخت افزار و سیستم عامل.
نکته: برای دستیابی به اطلاعات اضافه در رابطه با سیستم عامل از دستور `lsb_release` استفاده کنید.
اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/uname>.

- نمایش اطلاعات مربوط به سخت افزار و پردازنده سیستم:

`uname -mp`

- نمایش اطلاعات مربوط به نرم افزار از جمله: سیستم عامل، شماره انتشار و نسخه:

`uname -srv`

- نمایش نام سیستم:

`uname -n`

- نمایش تمامی اطلاعات سیستم(سخت افزار، نرم افزار، نام سیستم):

`uname -a`
