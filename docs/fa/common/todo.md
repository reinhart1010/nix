---
layout: page
title: common/todo (فارسی)
description: "ابزاری ساده و استاندارد برای مدیریت یادداشت و فهرست وظایف."
content_hash: a936a835d978c42d986bf1da8e6f00f26f6b0af3
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/todo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/todo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/todo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/todo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># todo

ابزاری ساده و استاندارد برای مدیریت یادداشت و فهرست وظایف.
اطلاعات بیشتر: <https://todoman.readthedocs.io>.

- لیست کارهای آغاز نشده:

`todo list --startable`

- اضافه کردن یک وظیفه به فهرست کارها :

`todo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thing_to_do</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">work</span>

- اضافه کردن مکان به یک وظیفه با آیدی:

`todo edit --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">location_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- نمایش جزییات یک وظیفه:

`todo show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- علامت زدن وظیفه ها با آیدی مشخص شده به عنوان تکمیل شده:

`todo done `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id1 task_id2 ...</span>

- حذف یک وظیفه:

`todo delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task_id</span>

- حذف وظایف انجام شده و بازشماری آیدی وظایف باقی مانده:

`todo flush`
