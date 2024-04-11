---
layout: page
title: common/atuin (فارسی)
description: "ذخیره سازی تاریخچه شل شما در یک دیتابیس قابل جستجو."
content_hash: b930bcc0f3a0898636e955d18b62255df25ce199
last_modified_at: 2024-04-11
related_topics:
  - title: English version
    url: /en/common/atuin.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atuin.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atuin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atuin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atuin

ذخیره سازی تاریخچه شل شما در یک دیتابیس قابل جستجو.
به صورت اختیاری می توانید تاریخچه رمزنگاری شده را بین دستگاه هایتان هماهنگ کنید.
اطلاعات بیشتر: <https://atuin.sh/docs/commands>.

- نصب آتویین برروی شل شما:

`eval "$(atuin init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish</span>`)"`

- وارد کردن تاریخچه از فایل مربوط به تاریخچه پیشفرض شل:

`atuin import auto`

- جستجوی تاریخچه شل برای یک دستور خاص:

`atuin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- ثبت نام یک حساب بر روی سرور پیشفرض با استفاده از نام کاربری و ایمیل و رمزعبور دلخواه:

`atuin register -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- ورود به سرور پیشفرض:

`atuin login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- هماهنگ کردن تاریخچه با سرور:

`atuin sync`
