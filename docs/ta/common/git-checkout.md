---
layout: page
title: common/git-checkout (தமிழ்)
description: "வேலை செய்யும் மரத்திற்கு ஒரு கிளை அல்லது பாதைகளை செக்கவுட் செய்ய."
content_hash: 172ef5254287ffe2de9d6c57139a0fc4777bfb44
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-checkout.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-checkout.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-checkout.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-checkout.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git checkout

வேலை செய்யும் மரத்திற்கு ஒரு கிளை அல்லது பாதைகளை செக்கவுட் செய்ய.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-checkout>.

- புதிய கிளையை உருவாக்கி மாறவும்:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>

- ஒரு குறிப்பிட்ட குறிப்பை அடிப்படையாகக் கொண்டு புதிய கிளையை உருவாக்கி மாறவும் (கிளை, தொலை / கிளை, குறிச்சொல் சரியான குறிப்புகளின் எடுத்துக்காட்டுகள்):

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிப்பு</span>

- ஏற்கனவே உள்ள உள்ளூர் கிளைக்கு மாறவும்:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>

- முன்பு செக்கவுட்ச்செய்யப்பட்ட கிளைக்கு மாறவும்:

`git checkout -`

- ஏற்கனவே உள்ள தொலை கிளைக்கு மாறவும்:

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தொலை_பெயர்</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>

- தற்போதைய கோப்பகத்தில் நிலையற்ற அனைத்து மாற்றங்களையும் நிராகரிக்கவும் (செயல்தவிர் போன்ற கட்டளைகளுக்கு `git reset` ஐப் பார்க்கவும்):

`git checkout .`

- கொடுக்கப்பட்ட கோப்பில் நிலையற்ற மாற்றங்களை நிராகரிக்கவும்:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_பெயர்</span>

- தற்போதைய கோப்பகத்தில் ஒரு கோப்பை ஒரு குறிப்பிட்ட கிளையில் செய்த பதிப்போடு மாற்றவும்:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கிளையின்_பெயர்</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_பெயர்</span>
