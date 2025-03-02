---
layout: page
title: linux/dialog (العربية)
description: "عرض نافذة حوار في الطرفية (Terminal)."
content_hash: 7d828070a9eb442b559aef7d8b08b053721e0eae
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/dialog.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dialog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dialog

عرض نافذة حوار في الطرفية (Terminal).
لمزيد من التفاصيل: <https://manned.org/dialog>.

- عرض رسالة:

`dialog --msgbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Message</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>

- مطالبة المستخدم بإدخال نص:

`dialog --inputbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Enter text:</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>` 2>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>

- مطالبة المستخدم بسؤال بنعم/لا:

`dialog --yesno "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Continue?</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40</span>
