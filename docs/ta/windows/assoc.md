---
layout: page
title: windows/assoc (தமிழ்)
description: "கோப்பு நீட்டிப்புகள் மற்றும் கோப்பு வகைகளுக்கு இடையே உள்ள தொடர்பைக் காட்டவும் அல்லது மாற்றவும்."
content_hash: 62a641088117774411fdf2fd547a8a59571ced3c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/assoc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/assoc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/assoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/assoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# assoc

கோப்பு நீட்டிப்புகள் மற்றும் கோப்பு வகைகளுக்கு இடையே உள்ள தொடர்பைக் காட்டவும் அல்லது மாற்றவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- கோப்பு நீட்டிப்புகள் மற்றும் கோப்பு வகைகளுக்கு இடையே உள்ள அனைத்து தொடர்புகளையும் பட்டியலிடுங்கள்:

`assoc`

- குறிப்பிட்ட நீட்டிப்புக்கான தொடர்புடைய கோப்பு வகையைக் காண்பி:

`assoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.txt</span>

- குறிப்பிட்ட நீட்டிப்புக்கு தொடர்புடைய கோப்பு வகையை அமைக்கவும்:

`assoc .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txtfile</span>

- ஒரு நேரத்தில் ஒரு திரையின் `assoc` வெளியீட்டைப் பார்க்கவும்:

`assoc | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">more</span>
