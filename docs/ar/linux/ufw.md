---
layout: page
title: linux/ufw (العربية)
description: "جدار حماية بسيط."
content_hash: 39cb4cbef5c13f547b9a6a3fa9b8a58c525761c7
last_modified_at: 2025-03-02
related_topics:
  - title: català version
    url: /ca/linux/ufw.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ufw.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ufw.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/ufw.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ufw.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/ufw.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/ufw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ufw

جدار حماية بسيط.
واجهة أمامية لـ `iptables` تهدف إلى تسهيل تكوين جدار الحماية.
لمزيد من التفاصيل: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- تفعيل ufw:

`ufw enable`

- تعطيل ufw:

`ufw disable`

- عرض قواعد ufw مع أرقامها:

`ufw status numbered`

- السماح بحركة المرور الواردة على المنفذ 5432 مع تعليق يحدد الخدمة:

`ufw allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5432</span>` comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Service</span>`"`

- السماح بحركة مرور TCP فقط من العنوان 192.168.0.4 إلى أي عنوان على هذا الجهاز، على المنفذ 22:

`ufw allow proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.4</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- منع حركة المرور على المنفذ 80 على هذا الجهاز:

`ufw deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- منع جميع حركة مرور UDP إلى المنافذ في النطاق 8412:8500:

`ufw deny proto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8412:8500</span>

- حذف قاعدة معينة. يمكن الحصول على رقم القاعدة من أمر `ufw status numbered`:

`ufw delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_number</span>
