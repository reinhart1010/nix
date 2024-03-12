---
layout: page
title: linux/pacman (فارسی)
description: "واحد مدیریت پکیج آرچ لینوکس"
content_hash: 68839b07c1a7816bc947a2be9004e79275329993
last_modified_at: 2024-03-12
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
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

واحد مدیریت پکیج آرچ لینوکس
همچنین : `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
برای دیدن دستور های معادل در سایر پکیج منیجر ها <https://wiki.archlinux.org/title/Pacman/Rosetta>.
اطلاعات بیشتر : <https://man.archlinux.org/man/pacman.8>.

- همگام سازی و بروز رسانی تمام پکیج ها:

`sudo pacman -Syu`

- نصب پکیج جدید:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- حذف یک پکیج به همراه وابستگی هاش:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- جستجو در دیتابیس برای پکیج هایی که با یک فایل خاص تعارض دارند:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_name</span>`"`

- لیست کردن پکیج های نصب شده با نسخه آنها:

`pacman -Q`

- لیست کردن تنها پکیج هایی که مستقیما نصب شده اند به همراه نسخه آنها:

`pacman -Qe`

- لیست کردن پکیج هایی که به عنوان وابستگی نصب شده اند اما توسط هیچ پکیجی استفاده نمیشوند:

`pacman -Qtdq`

- خالی کردن کل کش  `pacman`:

`sudo pacman -Scc`
