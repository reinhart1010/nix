---
layout: page
title: common/git-clone (தமிழ்)
description: "ஏற்கனவே உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்."
content_hash: 167ddf7324944aa38419417e5e378453d8c2ae11
last_modified_at: 2023-11-13
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
  - title: 한국어 version
    url: /ko/common/git-clone.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-clone.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clone.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-clone.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clone

ஏற்கனவே உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-clone>.

- ஏற்கனவே உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- ஏற்கனவே உள்ள களஞ்சியத்தை ஒரு குறிப்பிட்ட கோப்பகத்தில் குளோன் செய்யுங்கள்:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>

- இருக்கும் களஞ்சியத்தையும் அதன் துணை தொகுதிகளையும் குளோன் செய்யுங்கள்:

`git clone --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- கணினியில் உள்ள ஒரு களஞ்சியத்தை குளோன் செய்யுங்கள்:

`git clone -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கணினியில்/உள்ள/களஞ்சியத்தின்/பாதை</span>

- அமைதியாக குளோன்:

`git clone -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- இயல்புநிலை கிளையில் மிகச் சமீபத்திய 10 கமிட்டுகளை மட்டுமே பெறும் களஞ்சியத்தை குளோன் செய்யுங்கள் (நேரத்தைச் சேமிக்க பயனுள்ளதாக இருக்கும்):

`git clone --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- ஏற்கனவே உள்ள களஞ்சியத்தை குளோன் செய்து ஒரு குறிப்பிட்ட கிளையை மட்டும் பெறுங்கள்:

`git clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>` --single-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>

- ஒரு குறிப்பிட்ட SSH கட்டளையைப் பயன்படுத்தி ஏற்கனவே உள்ள களஞ்சியத்தை குளோன் செய்யவும்:

`git clone --config core.sshCommand="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh -i தனியார்_ssh_key/பாதை</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_களஞ்சிய_இடம்</span>
