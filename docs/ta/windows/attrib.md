---
layout: page
title: windows/attrib (தமிழ்)
description: "கோப்புகள் அல்லது கோப்பகங்களின் பண்புக்கூறுகளைக் காட்டவும் அல்லது மாற்றவும்."
content_hash: 827c30d4c31bf7f27d7f1522c8cc5e9acaa4f4ad
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/attrib.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/attrib.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/attrib.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/attrib.html
    icon: bi bi-globe
tldri18n_status: 2
---
# attrib

கோப்புகள் அல்லது கோப்பகங்களின் பண்புக்கூறுகளைக் காட்டவும் அல்லது மாற்றவும்.
மேலும் விவரத்திற்கு: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- தற்போதைய கோப்பகத்தில் கோப்புகளின் அனைத்து தொகுப்பு பண்புகளையும் காண்பி:

`attrib`

- ஒரு குறிப்பிட்ட கோப்பகத்தில் கோப்புகளின் அனைத்து செட் பண்புக்கூறுகளையும் காண்பி:

`attrib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்\பாதை</span>

- தற்போதைய கோப்பகத்தில் கோப்புகள் மற்றும் [d]அடைவுகளின் அனைத்து தொகுப்பு பண்புகளையும் காண்பி:

`attrib /d`

- தற்போதைய கோப்பகம் மற்றும் [கள்]உப்-கோப்பகங்களில் கோப்புகளின் அனைத்து செட் பண்புக்கூறுகளையும் காண்பி:

`attrib /s`

- கோப்புகள் அல்லது கோப்பகங்களில் `[r]ead-only` அல்லது `[a]rchive` அல்லது `[s]ystem` அல்லது `[h]idden` அல்லது `not content [i]nexed` பண்புக்கூறைச் சேர்க்கவும்:

`attrib +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு_அல்லது_அடைவு1 பாதை/டு/கோப்பு_அல்லது_அடைவு2 ...</span>

- கோப்புகள் அல்லது கோப்பகங்களின் குறிப்பிட்ட பண்புகளை அகற்றவும்:

`attrib -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு_அல்லது_அடைவு1 பாதை/டு/கோப்பு_அல்லது_அடைவு2 ...</span>
