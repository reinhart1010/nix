---
layout: page
title: common/newsboat (العربية)
description: "هو قارئ خلاصة آر إس إس للطرفية أو الكونسول."
content_hash: 2ab4fedfb4e895148b006169359201ebe462c9e9
last_modified_at: 2024-01-05
related_topics:
  - title: English version
    url: /en/common/newsboat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# newsboat

هو قارئ خلاصة آر إس إس للطرفية أو الكونسول.
لمزيد من التفاصيل: <https://newsboat.org/>.

- إستيراد روابط الخلاصات من ملف OPML:

`newsboat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-feeds.xml</span>

- إضافة روابط الخلاصات يدوياً:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/path/to/feed</span>` >> "${HOME}/.newsboat/urls"`

- إبدأ newsboat وقم بتحديث كل الخلاصات عند بدء التشغيل:

`newsboat -r`

- نفذ أمر أو عدة أوامر مفصولة بمسافات بدون الحاجة إلي فتح newsboat:

`newsboat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reload print-unread ...</span>

- انظر إختصارات لوحة المفاتيح (الإختصارت الأكثر شيوعاً مرئية في شريط الحالة):

`?`
