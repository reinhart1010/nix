---
layout: page
title: common/git-clean (தமிழ்)
description: "கண்காணிக்கப்படாத கோப்புகளை பணியிடத்திலிருந்து அகற்றவும்."
content_hash: fd9cfb4a79b6d1e37110db2e5bff70860a364781
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
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
---
# git clean

கண்காணிக்கப்படாத கோப்புகளை பணியிடத்திலிருந்து அகற்றவும்.
மேலும் விவரத்திற்கு: <https://git-scm.com/docs/git-clean>.

- கிட் மூலம் கண்காணிக்கப்படாத கோப்புகளை நீக்கு:

`git clean`

- கிட் மூலம் கண்காணிக்கப்படாத கோப்புகளை ஊடாடும் வகையில் நீக்கு:

`git clean -i`

- எந்த கோப்புகள் உண்மையில் நீக்கப்படாமல் நீக்கப்படும் என்பதைக் காட்டு:

`git clean --dry-run`

- கிட் மூலம் கண்காணிக்கப்படாத கோப்புகளை கட்டாயமாக நீக்கு:

`git clean -f`

- கிட் மூலம் கண்காணிக்கப்படாத கோப்பகங்களை கட்டாயமாக நீக்கு:

`git clean -fd`

- `.gitignore` மற்றும் `.git/info/exclude` ஆகியவற்றில் புறக்கணிக்கப்பட்ட கோப்புகள் உட்பட, தடமறியப்படாத கோப்புகளை நீக்கு:

`git clean -x`
