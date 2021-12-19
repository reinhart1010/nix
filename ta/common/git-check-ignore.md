---
layout: page
title: common/git-check-ignore (தமிழ்)
description: "(\".gitignore\") கோப்புகளை புறக்கணிக்கவும் / விலக்கவும் பகுப்பாய்வு செய்து பிழைத்திருத்தம் செய்யுங்கள்."
content_hash: a1d3d17d4dd9a1000ca130b4553e2dfd7cec5001
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
---
# git check-ignore

(".gitignore") கோப்புகளை புறக்கணிக்கவும் / விலக்கவும் பகுப்பாய்வு செய்து பிழைத்திருத்தம் செய்யுங்கள்.
மேலும் தகவல்: <https://git-scm.com/docs/git-check-ignore>.

- ஒரு கோப்பு அல்லது கோப்புறை புறக்கணிக்கப்பட்டுள்ளதா என சரிபார்க்கவும்:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_அல்லது_கோப்புறைக்கான/பாதை</span>

- பல கோப்புகள் அல்லது கோப்பகங்கள் புறக்கணிக்கப்படுகின்றனவா என்பதைச் சரிபார்க்கவும்:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான_பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புறைக்கான_பாதை</span>

- stdin இலிருந்து ஒரு வரியில் ஒன்றுக்கு பாதை பெயர்களைப் பயன்படுத்தவும்:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_பட்டியலுக்கான/பாதை</span>

- குறியீட்டை சரிபார்க்க வேண்டாம் (பாதைகள் ஏன் கண்காணிக்கப்பட்டன மற்றும் புறக்கணிக்கப்படவில்லை என்பதை பிழைத்திருத்த பயன்படுகிறது):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புகள்_அல்லது_கோப்புறைகளுக்கான/பாதை</span>

- ஒவ்வொரு பாதைக்கும் பொருந்தும் முறை பற்றிய விவரங்களைச் சேர்க்கவும்:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புகள்_அல்லது_கோப்புறைகளுக்கான/பாதை</span>
