---
layout: page
title: common/git-check-ignore (தமிழ்)
description: "(\".gitignore\") கோப்புகளை புறக்கணிக்கவும் / விலக்கவும் பகுப்பாய்வு செய்து பிழைத்திருத்தம் செய்யுங்கள்."
content_hash: a377b15cd974f391d52c9859d103afa11017da86
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/git-check-ignore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-check-ignore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-check-ignore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ignore

(".gitignore") கோப்புகளை புறக்கணிக்கவும் / விலக்கவும் பகுப்பாய்வு செய்து பிழைத்திருத்தம் செய்யுங்கள்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-check-ignore>.

- ஒரு கோப்பு அல்லது கோப்புறை புறக்கணிக்கப்பட்டுள்ளதா என சரிபார்க்கவும்:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_அடைவு/பாதை</span>

- பல கோப்புகள் அல்லது கோப்பகங்கள் புறக்கணிக்கப்படுகின்றனவா என்பதைச் சரிபார்க்கவும்:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>

- `stdin` இலிருந்து ஒரு வரியில் ஒன்றுக்கு பாதை பெயர்களைப் பயன்படுத்தவும்:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_பட்டியல்/பாதை</span>

- குறியீட்டை சரிபார்க்க வேண்டாம் (பாதைகள் ஏன் கண்காணிக்கப்பட்டன மற்றும் புறக்கணிக்கப்படவில்லை என்பதை பிழைத்திருத்த பயன்படுகிறது):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_அடைவு/பாதை</span>

- ஒவ்வொரு பாதைக்கும் பொருந்தும் முறை பற்றிய விவரங்களைச் சேர்க்கவும்:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_அடைவு/பாதை</span>
