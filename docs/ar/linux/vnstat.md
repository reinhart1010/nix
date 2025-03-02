---
layout: page
title: linux/vnstat (العربية)
description: "مراقبة حركة مرور الشبكة عن طريق وحدة تحكم."
content_hash: ee83bbad70d056ea3719f6dad4f00a6933c4d51c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/vnstat.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/vnstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/vnstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vnstat

مراقبة حركة مرور الشبكة عن طريق وحدة تحكم.
لمزيد من التفاصيل: <https://manned.org/vnstat>.

- عرض ملخص حركة المرور لجميع الواجهات:

`vnstat`

- عرض ملخص حركة المرور لواجهة شبكة محددة:

`vnstat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>

- عرض إحصائيات مباشرة لواجهة شبكة محددة:

`vnstat -l -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">network_interface</span>

- عرض إحصائيات حركة المرور على أساس كل ساعة خلال آخر 24 ساعة باستخدام رسم بياني شريطي:

`vnstat -hg`

- قياس وعرض متوسط حركة المرور لمدة 30 ثانية:

`vnstat -tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
