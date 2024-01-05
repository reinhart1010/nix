---
layout: page
title: linux/gpasswd (العربية)
description: "إدارة `/etc/group` و `/etc/gshadow`."
content_hash: a596bb4dee728dbe808e7ecf085b424b447318f7
last_modified_at: 2024-01-05
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

`sudo gpasswd -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user1,user2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- عين أعضاء المجموعة المسماة:

`sudo gpasswd -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user1,user2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- إنشئ رقم سري للمجموعة المسماة:

`gpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- أضف عضو إلي المجموعة المسماة:

`gpasswd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- إحذف عضو من المجموعة المسماة:

`gpasswd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>
