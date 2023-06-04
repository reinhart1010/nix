---
layout: page
title: common/javac (தமிழ்)
description: "ஜாவா பயன்பாட்டு தொகுப்பாளர்."
content_hash: 8059366a9c5519a7309970a5ad79dd0b5b08ad0a
last_modified_at: 2023-06-04
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

ஜாவா பயன்பாட்டு தொகுப்பாளர்.
மேலும் விவரத்திற்கு: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- ஒரு `.java` கோப்பை தொகுக்கவும்:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.java</span>

- பல `.java` கோப்புகளை தொகுக்கவும்:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு3.java</span>

- தற்போதைய கோப்பகத்தில் அனைத்து `.java` கோப்புகளையும் தொகுக்கவும்:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.java</span>

- ஒரு `.java` கோப்பை தொகுத்து அதன் விளைவாக வரும் கிளாஸ் கோப்பை ஒரு குறிப்பிட்ட கோப்பகத்தில் வைக்கவும்:

`javac -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.java</span>
