---
layout: page
title: common/git-add (தமிழ்)
description: "மாற்றப்பட்ட கோப்புகளை குறியீட்டில் சேர்க்கிறது."
content_hash: fb648b1521087b4200d2005080da38fea88f836e
last_modified_at: 2024-06-20
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git add

மாற்றப்பட்ட கோப்புகளை குறியீட்டில் சேர்க்கிறது.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-add>.

- குறியீட்டில் ஒரு கோப்பைச் சேர்க்க:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- எல்லா கோப்புகளையும் சேர்க்கவும் (கண்காணிக்கப்பட்ட மற்றும் தடமறியப்படாத):

`git add -A`

- ஏற்கனவே கண்காணிக்கப்பட்ட கோப்புகளை மட்டுமே சேர்க்கவும்:

`git add -u`

- புறக்கணிக்கப்பட்ட கோப்புகளையும் சேர்க்கவும்:

`git add -f`

- ஊடாடும் வகையில் சில கோப்புகளை சேர்க்கவும்:

`git add -p`

- கொடுக்கப்பட்ட கோப்பின் ஊடாடும் கட்ட பாகங்கள் சேர்க்கவும்:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- ஒரு கோப்பை ஊடாடும் வகையில் சேர்க்கவும்:

`git add -i`
