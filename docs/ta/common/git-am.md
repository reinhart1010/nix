---
layout: page
title: common/git-am (தமிழ்)
description: "பேட்ச் கோப்புகளைப் பயன்படுத்துங்கள். மின்னஞ்சல் வழியாக கமிட் பெறும்போது பயனுள்ளதாக இருக்கும்."
content_hash: a5855f3c2fd96030bdd24f7a033bf91d21218a44
last_modified_at: 2023-06-02
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
  - title: 한국어 version
    url: /ko/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-am.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git am

பேட்ச் கோப்புகளைப் பயன்படுத்துங்கள். மின்னஞ்சல் வழியாக கமிட் பெறும்போது பயனுள்ளதாக இருக்கும்.
பேட்ச் கோப்புகளை உருவாக்கக்கூடிய `git format-patch` கட்டளையை காண்க.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-am>.

- பேட்ச் கோப்பைப் பயன்படுத்துங்கள்:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.patch</span>

- ரிமோட் பேட்ச் கோப்பைப் பின்பற்றி, மாற்றங்களைச் செய்யுங்கள்:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- பேட்ச் கோப்பைப் பயன்படுத்துவதற்கான செயல்முறையை நிறுத்தவும்:

`git am --abort`

- கோப்புகளை நிராகரிக்க தோல்வியுற்ற ஹன்களை சேமித்து, முடிந்தவரை ஒரு பேட்ச் கோப்பைப் பயன்படுத்துங்கள்:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.patch</span>
