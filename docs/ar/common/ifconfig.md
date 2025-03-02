---
layout: page
title: common/ifconfig (العربية)
description: "مُكوِّن واجهة الشبكة."
content_hash: 2b23c189393cedbbc546585e94261dd2b76a9624
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ifconfig.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ifconfig.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ifconfig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ifconfig.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ifconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ifconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifconfig

مُكوِّن واجهة الشبكة.
لمزيد من التفاصيل: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- عرض إعدادات الشبكة لواجهة محددة:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>

- عرض تفاصيل جميع الواجهات، بما في ذلك الواجهات المعطلة:

`ifconfig -a`

- تعطيل واجهة محددة:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` down`

- تمكين واجهة محددة:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` up`

- تعيين عنوان IP لواجهة محددة:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>
