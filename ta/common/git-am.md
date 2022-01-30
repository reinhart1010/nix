---
layout: page
title: common/git-am (தமிழ்)
description: "பேட்ச் கோப்புகளைப் பயன்படுத்துங்கள். மின்னஞ்சல் வழியாக கமிட் பெறும்போது பயனுள்ளதாக இருக்கும்."
content_hash: c5db732faad5586de4c9e7b2142f4bcdcaaa80ac
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
---
# git am

பேட்ச் கோப்புகளைப் பயன்படுத்துங்கள். மின்னஞ்சல் வழியாக கமிட் பெறும்போது பயனுள்ளதாக இருக்கும்.
பேட்ச் கோப்புகளை உருவாக்கக்கூடிய `git format-patch` கட்டளையை காண்க.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-am>.

- பேட்ச் கோப்பைப் பயன்படுத்துங்கள்:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை/கோப்பு.patch</span>

- பேட்ச் கோப்பைப் பயன்படுத்துவதற்கான செயல்முறையை நிறுத்தவும்:

`git am --abort`

- கோப்புகளை நிராகரிக்க தோல்வியுற்ற ஹன்களை சேமித்து, முடிந்தவரை ஒரு பேட்ச் கோப்பைப் பயன்படுத்துங்கள்:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புக்கான/பாதை/கோப்பு.patch</span>
