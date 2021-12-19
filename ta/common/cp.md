---
layout: page
title: common/cp (தமிழ்)
description: "கோப்புகளையோ அடைவுகளையோ நகலெடு."
content_hash: cade69d2eb30405000f96db33267ac5026e88f48
related_topics:
  - title: Deutsch version
    url: /de/common/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
---
# cp

கோப்புகளையோ அடைவுகளையோ நகலெடு.
மேலும் தகவல்: <https://www.gnu.org/software/coreutils/cp>.

- கோப்பை நகலெடு:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பிற்குப்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/கோப்பிற்குப்/பாதை</span>

- கோப்பை நகலெடுத்து அடைவொன்றிற்குள் அதே பெயருடன் வை:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பிற்குப்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/கோப்பின்/தாயடைவிற்குப்/பாதை</span>

- அடைவையும் அதில் உள்ளடங்கிய அனைத்தையும் தற்சுருளாக நகலெடு:

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல/அடைவிற்குப்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>

- அடைவையும் அதில் உள்ளடங்கிய அனைத்தையும் தற்சுருளாக வளவள நிலையில் (நகலெடுக்கப்படும் கோப்புகள் பட்டியலிடப்படும்) நகலெடு:

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல/அடைவிற்குப்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>

- அடைவின் உள்ளடக்கத்தை நகலெடுத்து இன்னொரு அடைவிற்குள் வை:

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல/அடைவிற்குப்/பாதை/*</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>

- txt வகைப்பெயருடையக் கோப்புகளை ஊடாட்ட நிலையில் (ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் உறுதிப்படுத்தக் கேட்கும்) நகலெடு:

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>
