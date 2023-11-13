---
layout: page
title: windows/comp (தமிழ்)
description: "இரண்டு கோப்புகள் அல்லது கோப்புகளின் தொகுப்புகளின் உள்ளடக்கங்களை ஒப்பிடுக."
content_hash: f5f242ffc492750a71d2f4b8afafee644bc0809d
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/windows/comp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/comp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comp

இரண்டு கோப்புகள் அல்லது கோப்புகளின் தொகுப்புகளின் உள்ளடக்கங்களை ஒப்பிடுக.
கோப்புகளின் தொகுப்புகளை ஒப்பிட, வைல்டு கார்டுகளைப் (*) பயன்படுத்தவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- கோப்புகளை ஊடாடும் வகையில் ஒப்பிடுக:

`comp`

- இரண்டு குறிப்பிட்ட கோப்புகளை ஒப்பிடுக:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_1\பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_2\பாதை</span>

- இரண்டு செட் கோப்புகளை ஒப்பிடுக:

`comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவு_1\பாதை</span>`\* `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவு_2\பாதை</span>`\*`

- தசம வடிவத்தில் வேறுபாடுகளைக் காண்பி:

`comp /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_1\பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_2\பாதை</span>

- ASCII வடிவத்தில் வேறுபாடுகளைக் காண்பி:

`comp /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_1\பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_2\பாதை</span>

- வேறுபாடுகளுக்கான வரி எண்களைக் காண்பி:

`comp /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_1\பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_2\பாதை</span>

- கோப்புகளை கேஸ்-உணர்வின்றி ஒப்பிடுக:

`comp /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_1\பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_2\பாதை</span>

- ஒவ்வொரு கோப்பின் முதல் 5 வரிகளை மட்டும் ஒப்பிடுக:

`comp /n=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_1\பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_2\பாதை</span>
