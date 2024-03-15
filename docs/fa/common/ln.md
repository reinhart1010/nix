---
layout: page
title: common/ln (فارسی)
description: "این دستور برای ایجاد ارتباط(link) به فایل ها و پوشه ها(Directories) استفاده می شود."
content_hash: 9131272ba9569c85a71bc7937384ba731333dbd0
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ln.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ln.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ln.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ln.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ln.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ln

این دستور برای ایجاد ارتباط(link) به فایل ها و پوشه ها(Directories) استفاده می شود.
اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/ln>.

- ایجاد یک ارتباط نمادین (symbolic link) به یک فایل یا پوشه:

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>

- جایگزینی یک ارتباط نمادین موجود، برای اشاره به یک فایل متفاوت:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/new_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>

- ایجاد یک لینک سخت (hard link) به یک فایل:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/hardlink</span>
