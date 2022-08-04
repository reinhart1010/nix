---
layout: page
title: common/java (தமிழ்)
description: "ஜாவா பயன்பாட்டு துவக்கி."
content_hash: 81cc14d4d8d6b95f1eda66311941369dc6ef8156
related_topics:
  - title: English version
    url: /en/common/java.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/java.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/java.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/java.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/java.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># java

ஜாவா பயன்பாட்டு துவக்கி.
மேலும் விவரத்திற்கு: <https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html>.

- ஒரு main செயல்பாட்டைக் கொண்ட ஜாவா .class கோப்பை வெறும் class பெயரை பயன்படுத்தி இயக்கவும்:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class_பெயரை</span>

- ஒரு .jar நிரலை இயக்கவும்:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோபின்_பெயர்.jar</span>

- போர்ட் 5005 இல் இணைக்க காத்திருக்கும் பிழைதிருத்தி .jar நிரலை இயக்கவும்:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோபின்_பெயர்.jar</span>

- JDK, JRE மற்றும் HotSpot மென்பொருள் பதிப்புகள் காண்பி:

`java -version`

- java கட்டளைக்கான பயன்பாட்டு தகவலை காண்பி:

`java -help`
