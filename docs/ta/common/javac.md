---
layout: page
title: common/javac (தமிழ்)
description: "ஜாவா நிரல்மொழிமாற்றி."
content_hash: d67c55a938981df376b37a4b8d0583685296f460
related_topics:
  - title: English version
    url: /en/common/javac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/javac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/javac.html
    icon: bi bi-globe
---
# javac

ஜாவா நிரல்மொழிமாற்றி.
மேலும் விவரத்திற்கு: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/javac.html>.

- `.java` கோப்பை நிரல்மொழிமாற்ற:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.java</span>

- பல `.java` கோப்புகளை நிரல்மொழிமாற்ற:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு3.java</span>

- தற்போதைய கோப்பகத்தில் அனைத்து `.java` கோப்புகளையும் நிரல்மொழிமாற்ற:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.java</span>

- ஒரு `.java` கோப்பை நிரல்மொழிமாற்றி, அதன் விளைவாக வரும் `.class` கோப்பை ஒரு குறிப்பிட்ட கோப்பகத்தில் வைக்கவும்:

`javac -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்புறையை/குறிவைக்கும்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.java</span>
