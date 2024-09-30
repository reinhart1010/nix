---
layout: page
title: common/git-clean (தமிழ்)
description: "கண்காணிக்கப்படாத கோப்புகளை பணியிடத்திலிருந்து அகற்றவும்."
content_hash: 9798b95222c74c21fcbd89a123377fe7964f8006
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clean

கண்காணிக்கப்படாத கோப்புகளை பணியிடத்திலிருந்து அகற்றவும்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-clean>.

- கிட் மூலம் கண்காணிக்கப்படாத கோப்புகளை நீக்கு:

`git clean`

- கிட் மூலம் கண்காணிக்கப்படாத கோப்புகளை ஊடாடும் வகையில் நீக்கு:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>

- எந்த கோப்புகள் உண்மையில் நீக்கப்படாமல் நீக்கப்படும் என்பதைக் காட்டு:

`git clean --dry-run`

- கிட் மூலம் கண்காணிக்கப்படாத கோப்புகளை கட்டாயமாக நீக்கு:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- கிட் மூலம் கண்காணிக்கப்படாத கோப்பகங்களை கட்டாயமாக நீக்கு:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` -d`

- `.gitignore` மற்றும் `.git/info/exclude` ஆகியவற்றில் புறக்கணிக்கப்பட்ட கோப்புகள் உட்பட, தடமறியப்படாத கோப்புகளை நீக்கு:

`git clean -x`
