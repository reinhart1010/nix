---
layout: page
title: common/cppclean (فارسی)
description: "پیدا کردن کد های بدون استفاده در پروژه های سی پلاس پلاس."
content_hash: 3c6e6263e2d7c989d661480730946fe8016e9239
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/cppclean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cppclean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cppclean.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cppclean.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cppclean

پیدا کردن کد های بدون استفاده در پروژه های سی پلاس پلاس.
اطلاعات بیشتر: <https://github.com/myint/cppclean>.

- اجرا در پوشه ی پروژه:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- اجرا روی پروژه درحالی که هدرها در پوشه های `inc1/` و `inc2/` قرار دارند:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>` --include-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc1</span>` --include-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc2</span>

- اجرا روی فایل دلخواه مانند `main.cpp`:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main.cpp</span>

- اجرا روی پوشه کنونی به استثنای پوشه "build":

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` --exclude=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>
