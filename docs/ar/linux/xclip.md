---
layout: page
title: linux/xclip (العربية)
description: "أداة معالجة لحافظة x11، تشبه إلي حد ما `xsel`."
content_hash: 6eddadb628d21300e05ccf726a547865f26a121a
last_modified_at: 2024-01-05
related_topics:
  - title: English version
    url: /en/linux/xclip.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/xclip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xclip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xclip

أداة معالجة لحافظة x11، تشبه إلي حد ما `xsel`.
تتعامل مع الحافظة الأولية والثانوية لـ x، بالإضافة إلي حافظة النظام (`Ctrl + C`/`Ctrl + V`).
لمزيد من التفاصيل: <https://manned.org/xclip>.

- إنسخ ناتج الخرج من أمر إلي حافظة x11 الأولية:

`echo 123 | xclip`

- إنسخ ناتج الخرج من أمر إلي الحافظة المختارة:

`echo 123 | xclip -selection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|secondary|clipboard</span>

- إنسخ ناتج الخرج من أمر إلي حافظة النظام، باستخدام الصيغة المختصرة:

`echo 123 | xclip -sel clip`

- إنسخ محتوي ملف إلي حافظة النظام:

`xclip -sel clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.txt</span>

- إنسخ محتوي صورة بصيغة PNG إلي حافظة النظام (يمكن أن تستخدم في أي برنامج عن طريق لصق):

`xclip -sel clip -t image/png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.png</span>

- إنسخ إدخال المستخدم في الطرفية أو الكونسول إلي حافظة النظام:

`xclip -i`

- إلصق محتوي حافظة x11 الأولية إلي الطرفية أو الكونسول:

`xclip -o`

- إلصق محتوي حافظة النظام إلي الطرفية أو الكونسول:

`xclip -o -sel clip`
