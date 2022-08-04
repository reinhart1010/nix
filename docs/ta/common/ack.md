---
layout: page
title: common/ack (தமிழ்)
description: "புரோகிராமர்களுக்கு உகந்ததாக கிரப் போன்ற தேடல் கருவி."
content_hash: 95d4dc037238574e80fb332b91203b55409173e8
related_topics:
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ack

புரோகிராமர்களுக்கு உகந்ததாக கிரப் போன்ற தேடல் கருவி.
மேலும் விவரத்திற்கு: <https://beyondgrep.com/documentation>.

- "காலை" கொண்ட கோப்புகளைக் கண்டறியவும்:

`ack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">காலை</span>

- ஒரு குறிப்பிட்ட வகை கோப்புகளைக் கண்டறியவும்:

`ack --ruby `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">காலை</span>

- "காலை" என்ற சொல்லின் மொத்த பொருத்தங்களை எண்ணிக்கையை எண்ணவும்:

`ack -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">காலை</span>

- காலை என்னும் சொல்லை கொண்ட ஒவ்வொரு கோப்பின் பெயர் மற்றும் பொருத்தங்களின் எண்ணிக்கையை காட்டவும்:

`ack -cl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">காலை</span>

- அனைத்து செல்லுபடியாகும் வகைகளையும் பட்டியலிடவும்:

`ack --help-types`
