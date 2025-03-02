---
layout: page
title: common/tr (العربية)
description: "ترجمة الأحرف: تنفيذ عمليات الاستبدال بناءً على أحرف مفردة ومجموعات أحرف."
content_hash: 2832f058fd0a93216213726d74df867dd33d4e8e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tr

ترجمة الأحرف: تنفيذ عمليات الاستبدال بناءً على أحرف مفردة ومجموعات أحرف.
لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- استبدال جميع تكرارات حرف معين في ملف وطباعة النتيجة:

`tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_character</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_character</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- استبدال جميع تكرارات حرف معين من ناتج أمر آخر:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` | tr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find_character</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">replace_character</span>

- تعيين كل حرف من المجموعة الأولى إلى الحرف المقابل في المجموعة الثانية:

`tr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abcd</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jkmn</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- حذف جميع تكرارات مجموعة الأحرف المحددة من المدخلات:

`tr -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_characters</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- ضغط سلسلة من الأحرف المتطابقة إلى حرف واحد:

`tr -s '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_characters</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- ترجمة محتويات ملف إلى أحرف كبيرة (Upper-case):

`tr "[:lower:]" "[:upper:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- إزالة الأحرف غير القابلة للطباعة من ملف:

`tr -cd "[:print:]" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
