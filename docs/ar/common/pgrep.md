---
layout: page
title: common/pgrep (العربية)
description: "البحث عن العمليات أو إرسال إشارات إليها باستخدام الاسم."
content_hash: 2c7338f88c14e5cbec7afae792f19afd2672a22b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pgrep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pgrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pgrep

البحث عن العمليات أو إرسال إشارات إليها باستخدام الاسم.
لمزيد من التفاصيل: <https://www.manned.org/pgrep>.

- عرض معرّفات العمليات (PIDs) لأي عمليات جارية تتطابق مع اسم العملية:

`pgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>

- البحث عن العمليات مع الخيارات المستخدمة في سطر الأوامر:

`pgrep --full "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameter</span>`"`

- البحث عن العمليات التي يتم تشغيلها بواسطة مستخدم معين:

`pgrep --euid root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
