---
layout: page
title: common/cut (العربية)
description: "استخراج حقول من `stdin` أو من الملفات."
content_hash: 9546558a848def663c4996705c1e2b0872ba0aae
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/cut.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cut.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

استخراج حقول من `stdin` أو من الملفات.
لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- طباعة نطاق [c]حرف/[f]حقل محدد من كل سطر:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters|fields</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- طباعة نطاق [f]حقل محدد من كل سطر باستخدام [d]فاصل معين:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --delimiter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" --fields `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- طباعة نطاق [c]حرف معين من كل سطر في ملف محدد:

`cut --characters `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- طباعة [f]حقول محددة من أسطر منتهية بـ `NUL` (مثل الناتج من `find . -print0`) بدلاً من أسطر جديدة:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --zero-terminated --fields `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
