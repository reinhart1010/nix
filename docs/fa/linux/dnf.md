---
layout: page
title: linux/dnf (فارسی)
description: "ابزار مدیریت بسته‌ها برای RHEL، Fedora و CentOS (جایگزین `yum`)."
content_hash: 6bf6776a576fda8c22b1a7c3d4a902505b23d61f
last_modified_at: 2024-01-05
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf

ابزار مدیریت بسته‌ها برای RHEL، Fedora و CentOS (جایگزین `yum`).
برای دستورات معادل در دیگر مدیران بسته، به <https://wiki.archlinux.org/title/Pacman/Rosetta> مراجعه کنید.
اطلاعات بیشتر: <https://dnf.readthedocs.io>.

- ارتقاء بسته‌های نصب شده به جدیدترین نسخه‌های موجود:

`sudo dnf upgrade`

- جستجوی بسته‌ها بر اساس کلمات کلیدی:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword1 keyword2 ...</span>

- نمایش جزئیات یک بسته:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- نصب یک بسته جدید (از `-y` برای تأیید اتوماتیک تمام پنجره‌ها استفاده کنید):

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- حذف یک بسته:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- لیست بسته‌های نصب شده:

`dnf list --installed`

- یافتن بسته‌هایی که دستور مشخصی را ارائه می‌دهند:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- مشاهده تاریخچه تمام عملیات‌های گذشته:

`dnf history`
