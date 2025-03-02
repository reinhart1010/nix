---
layout: page
title: common/openssl-x509 (العربية)
description: "أمر OpenSSL لإدارة شهادات X.509."
content_hash: 7e432af4f56dbe192b942009543543d0f6d2c17c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/openssl-x509.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/openssl-x509.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openssl x509

أمر OpenSSL لإدارة شهادات X.509.
لمزيد من التفاصيل: <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html>.

- عرض معلومات الشهادة:

`openssl x509 -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.crt</span>` -noout -text`

- عرض تاريخ انتهاء صلاحية الشهادة:

`openssl x509 -enddate -noout -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pem</span>

- تحويل الشهادة بين الترميز الثنائي DER والترميز النصي PEM:

`openssl x509 -inform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">der</span>` -outform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pem</span>` -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">original_certificate_file</span>` -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">converted_certificate_file</span>

- تخزين المفتاح العام للشهادة في ملف:

`openssl x509 -in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificate_file</span>` -noout -pubkey -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>
