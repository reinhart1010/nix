---
layout: page
title: common/fastmod (العربية)
description: "أداة للاستبدال الجزئي للنصوص في قاعدة الأكواد لديك."
content_hash: 947d68d6119e3a91e8e7c5583ac5eb5b7f47ac20
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/fastmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastmod

أداة للاستبدال الجزئي للنصوص في قاعدة الأكواد لديك.
التعبيرات النمطية يعالجها قفص من بضاعة رست وهو regex.
لمزيد من التفاصيل: <https://github.com/facebookincubator/fastmod>.

- استبدال بالتعبيرات النمطية في كل ملفات المسار الحالي وأبنائه في الملفات غير المُتجاهلة بـ .ignore أو .gitignore:

`fastmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">تعبير_نمطي</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">بديل</span>

- استبدال متجاهلا حالة الحرف في ملف أو في ملفات مسار:

`fastmod --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">تعبير_نمطي</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">بديل</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسار/الـ/ملف مسار/الـ/السجل ...</span>

- استبدال بالتعبيرات النمطية مع تحديد المكان الذي يُستبدل فيه:

`fastmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">تعبير_نمطي</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">بديل</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">مسار/للـ/سجل</span>` --iglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'**/*.{js,json}'</span>

- استبدال بالنص مُطابقةً (وليس التعبيرات النمطية)، في ملفات امتداداتهم إما js أو json فحسب:

`fastmod --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نص_مطابِق</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">بديل</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json,js</span>

- استبدال بجميع النصوص مُطابقةً، مباشرة دون مِحَثِّ تأكيد (prompt):

`fastmod --accept-all --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نص_مطابِق</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">بديل</span>

- استبدال بجميع النصوص مُطابقةً، مباشرة دون تأكيد، مع طباعة الملفات المُستبدل فيها:

`fastmod --accept-all --print-changed-files --fixed-strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">نص_مطابِق</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">بديل</span>
