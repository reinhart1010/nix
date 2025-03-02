---
layout: page
title: common/chisel (العربية)
description: "إنشاء أنفاق TCP/UDP، يتم نقلها عبر HTTP، وتأمينها عبر SSH."
content_hash: aba7fabcbea2fe0cdbd920a768f62cae270acaf4
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/chisel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chisel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chisel

إنشاء أنفاق TCP/UDP، يتم نقلها عبر HTTP، وتأمينها عبر SSH.
يتضمن كل من العميل والخادم في نفس الملف التنفيذي `chisel`.
لمزيد من التفاصيل: <https://github.com/jpillora/chisel>.

- تشغيل خادم Chisel:

`chisel server`

- تشغيل خادم Chisel يستمع إلى منفذ محدد:

`chisel server -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_port</span>

- تشغيل خادم Chisel يقبل الاتصالات المصادق عليها باستخدام اسم المستخدم وكلمة المرور:

`chisel server --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- الاتصال بخادم Chisel وإنشاء نفق لمنفذ محدد إلى خادم طرف ثالث ومنفذ:

`chisel client `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_server</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- الاتصال بخادم Chisel وإنشاء نفق لجهاز ومنفذ محددين إلى خادم طرف ثالث ومنفذ:

`chisel client `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_server</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- الاتصال بخادم Chisel باستخدام المصادقة باسم المستخدم وكلمة المرور:

`chisel client --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_server</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- تهيئة خادم Chisel في الوضع العكسي على منفذ محدد، مع تمكين وظيفة وكيل SOCKS5 (على المنفذ 1080):

`chisel server -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_port</span>` --reverse --socks5`

- الاتصال بخادم Chisel على عنوان IP ومنفذ محددين، وإنشاء نفق عكسي يتم تعيينه إلى وكيل SOCKS محلي:

`chisel client `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_port</span>` R:socks`
