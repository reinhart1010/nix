---
layout: page
title: common/openssl-req (العربية)
description: "أمر OpenSSL لإدارة طلبات توقيع الشهادات PKCS#10."
content_hash: 43249aedee030ee6e77aa710d28662953c85181d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/openssl-req.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/openssl-req.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openssl req

أمر OpenSSL لإدارة طلبات توقيع الشهادات PKCS#10.
لمزيد من التفاصيل: <https://www.openssl.org/docs/manmaster/man1/openssl-req.html>.

- إنشاء طلب توقيع شهادة لإرساله إلى جهة تصديق:

`openssl req -new -sha256 -key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.key</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.csr</span>

- إنشاء شهادة موقعة ذاتيًا وزوج مفاتيح مقابلة، وحفظهما في ملف:

`openssl req -new -x509 -newkey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` -keyout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.key</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.cert</span>` -subj "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/C=XX/CN=foobar</span>`" -days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">365</span>
