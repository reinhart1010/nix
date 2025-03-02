---
layout: page
title: common/tcpdump (العربية)
description: "عرض وتحليل حركة المرور على الشبكة."
content_hash: eeec6ed6e7961683d1c4cb36a8fd1f219e4f128d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tcpdump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tcpdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcpdump

عرض وتحليل حركة المرور على الشبكة.
لمزيد من التفاصيل: <https://www.tcpdump.org>.

- عرض قائمة بواجهات الشبكة المتوفرة:

`tcpdump -D`

- التقاط حركة المرور لواجهة شبكة محددة:

`tcpdump -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- التقاط جميع حركة مرور TCP مع عرض المحتويات (ASCII) في وحدة التحكم:

`tcpdump -A tcp`

- التقاط حركة المرور من أو إلى مضيف محدد:

`tcpdump host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- التقاط حركة المرور من واجهة معينة مع مصدر، وجهة ومنفذ وجهة محددين:

`tcpdump -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>` and dst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.2</span>` and dst port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>

- التقاط حركة المرور لشبكة محددة:

`tcpdump net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.0/24</span>

- التقاط جميع حركة المرور باستثناء حركة المرور على المنفذ 22 وحفظها في ملف:

`tcpdump -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile.pcap</span>` port not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22</span>

- قراءة البيانات من ملف محدد:

`tcpdump -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dumpfile.pcap</span>
