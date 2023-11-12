---
layout: page
title: linux/gpasswd (العربية)
description: "إدارة `/etc/group` و `/etc/gshadow`."
content_hash: 161fd4a5ebc24d8e3e562680f5000252dac83bdc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/gpasswd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpasswd

إدارة `/etc/group` و `/etc/gshadow`.
لمزيد من التفاصيل: <https://manned.org/gpasswd>.

- عرّف مديرين المجموعة المسماة:

`sudo gpasswd -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مدير 2, مدير 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مجموعة</span>

- عين أعضاء المجموعة المسماة:

`sudo gpasswd -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">عضو 2, عضو 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مجموعة</span>

- إنشئ رقم سري للمجموعة المسماة:

`gpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مجموعة</span>

- أضف عضو إلي المجموعة المسماة:

`gpasswd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">عضو</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مجموعة</span>

- إحذف عضو من المجموعة المسماة:

`gpasswd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">عضو</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مجموعة</span>
