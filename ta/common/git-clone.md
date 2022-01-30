---
layout: page
title: common/git-clone (தமிழ்)
description: "ஏற்கனவே உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்."
content_hash: 8934b30afac5a8276234680c1ecb7524845ade12
related_topics:
  - title: Deutsch version
    url: /de/common/git-clone.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-clone.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clone.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clone.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clone.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clone.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clone.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-clone.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git clone

ஏற்கனவே உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-clone>.

- ஏற்கனவே உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- இருக்கும் களஞ்சியத்தையும் அதன் துணை தொகுதிகளையும் குளோன் செய்யுங்கள்:

`git clone --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- கணினியில் உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்:

`git clone -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கணினியில்/உள்ள/களஞ்சியத்தின்/பாதை</span>

- அமைதியாக குளோன்:

`git clone -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- இயல்புநிலை கிளையில் மிகச் சமீபத்திய 10 கமிட்டுகளை மட்டுமே பெறும் களஞ்சியத்தை குளோன் செய்யுங்கள் (நேரத்தைச் சேமிக்க பயனுள்ளதாக இருக்கும்):

`git clone --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>
