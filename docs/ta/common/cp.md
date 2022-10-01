---
layout: page
title: common/cp (தமிழ்)
description: "கோப்புகளையோ அடைவுகளையோ நகலெடு."
content_hash: 0d813758bdc7a8bd32211f89c21df81733ddaacb
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
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
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/cp>.

- கோப்பை நகலெடு:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல_கோப்பு.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நகல்_கோப்பு.ext</span>

- கோப்பை நகலெடுத்து அடைவொன்றிற்குள் அதே பெயருடன் வை:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூல_கோப்பு.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/கோப்பின்/தாயடைவிற்குப்/பாதை</span>

- ஒரு கோப்பகத்தின் உள்ளடக்கங்களை மீண்டும் மீண்டும் மற்றொரு இடத்திற்கு நகலெடுக்கவும் (இலக்கு இருந்தால், அடைவு அதன் உள்ளே நகலெடுக்கப்படும்):

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல/அடைவிற்குப்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>

- ஒரு கோப்பகத்தை மீண்டும் மீண்டும், வாய்மொழி முறையில் நகலெடுக்கவும் (அவை நகலெடுக்கப்பட்ட கோப்புகளைக் காட்டுகிறது):

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூல/அடைவிற்குப்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>

- txt வகைப்பெயருடையக் கோப்புகளை ஊடாட்ட நிலையில் (ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் உறுதிப்படுத்தக் கேட்கும்) நகலெடு:

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>

- நகலெடுக்கும் முன் குறியீட்டு இணைப்புகளைப் பின்பற்றவும்:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இணைப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நகல்/அடைவிற்குப்/பாதை</span>
