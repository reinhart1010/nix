---
layout: page
title: linux/xclip (العربية)
description: "أداة معالجة لحافظة x11، تشبه إلي حد ما `xsel`."
content_hash: 9f156dc7e3987248b44fabe85b7cd747d169fb0e
related_topics:
  - title: English version
    url: /en/linux/xclip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/xclip.html
    icon: bi bi-globe
---
# xclip

أداة معالجة لحافظة x11، تشبه إلي حد ما `xsel`.
تتعامل مع الحافظة الأولية والثانوية لـ x، بالإضافة إلي حافظة النظام (`Ctrl + C`/`Ctrl + V`).

- إنسخ ناتج الخرج من أمر إلي حافظة x11 الأولية:

`echo 123 | xclip`

- إنسخ ناتج الخرج من أمر إلي الحافظة المختارة:

`echo 123 | xclip -selection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|secondary|clipboard</span>

- إنسخ ناتج الخرج من أمر إلي حافظة النظام، باستخدام الصيغة المختصرة:

`echo 123 | xclip -sel clip`

- إنسخ محتوي ملف إلي حافظة النظام:

`xclip -sel clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">اسم_الملف.txt</span>

- إنسخ محتوي صورة بصيغة PNG إلي حافظة النظام (يمكن أن تستخدم في أي برنامج عن طريق لصق):

`xclip -sel clip -t image/png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">اسم_الملف.png</span>

- إنسخ إدخال المستخدم في الطرفية أو الكونسول إلي حافظة النظام:

`xclip -i`

- إلصق محتوي حافظة x11 الأولية إلي الطرفية أو الكونسول:

`xclip -o`

- إلصق محتوي حافظة النظام إلي الطرفية أو الكونسول:

`xclip -o -sel clip`
