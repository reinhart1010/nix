---
layout: page
title: common/git-annex (தமிழ்)
description: "கோப்புகளை அவற்றின் உள்ளடக்கங்களை சரிபார்க்காமல், ஜிட் மூலம் நிர்வகிக்கவும்."
content_hash: 79d57863c16637a3556c4efbc4fb96ee897d9f8b
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/git-annex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-annex.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git annex

கோப்புகளை அவற்றின் உள்ளடக்கங்களை சரிபார்க்காமல், ஜிட் மூலம் நிர்வகிக்கவும்.
ஒரு கோப்பு இணைக்கப்படும்போது, ​​அதன் உள்ளடக்கம் ஒரு முக்கிய மதிப்புக் கடைக்கு நகர்த்தப்படும், மேலும் உள்ளடக்கத்தை சுட்டிக்காட்டும் ஒரு சிம்லிங்க் செய்யப்படுகிறது.
மேலும் விவரத்திற்கு: <https://git-annex.branchable.com>.

- `git annex` உடன் ஒரு களஞ்சியத்தை தொடங்கவும்:

`git annex init`

- ஒரு கோப்பைச் சேர்க்கவும்:

`git annex add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_அடைவு/பாதை</span>

- ஒரு கோப்பு அல்லது கோப்பகத்தின் தற்போதைய நிலையைக் காட்டு:

`git annex status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_அடைவு/பாதை</span>

- தொலைநிலையுடன் உள்ளூர் களஞ்சியத்தை ஒத்திசைக்கவும்:

`git annex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலைநிலை</span>

- ஒரு கோப்பு அல்லது கோப்பகத்தைப் பெறுங்கள்:

`git annex get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_அடைவு/பாதை</span>

- உதவியைக் காட்டு:

`git annex help`
