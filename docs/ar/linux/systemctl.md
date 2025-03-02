---
layout: page
title: linux/systemctl (العربية)
description: "التحكم في مدير نظام systemd والخدمات."
content_hash: 7e786de600019084ab53d41fc8f1709c7dd86a8b
last_modified_at: 2025-03-02
related_topics:
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/systemctl.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/systemctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/systemctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/systemctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/systemctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemctl

التحكم في مدير نظام systemd والخدمات.
لمزيد من التفاصيل: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- عرض جميع الخدمات قيد التشغيل:

`systemctl status`

- عرض الوحدات الفاشلة:

`systemctl --failed`

- بدء/إيقاف/إعادة تشغيل/إعادة تحميل/عرض حالة خدمة:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload|status</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- تمكين/تعطيل وحدة ليتم تشغيلها عند بدء تشغيل النظام:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- إعادة تحميل systemd والبحث عن وحدات جديدة أو متغيرة:

`systemctl daemon-reload`

- التحقق مما إذا كانت الوحدة نشطة/مُمكّنة/فاشلة:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is-active|is-enabled|is-failed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- عرض جميع وحدات الخدمة/المقبس/التركيب التلقائي مع التصفية حسب الحالة (قيد التشغيل/فاشلة):

`systemctl list-units --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service|socket|automount</span>` --state=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">failed|running</span>

- عرض محتويات ومسار ملف الوحدة:

`systemctl cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>
