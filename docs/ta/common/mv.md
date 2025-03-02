---
layout: page
title: common/mv (தமிழ்)
description: "கோப்புகளையோ அடைவுகளையோ நகர்த்து அல்லது மறுபெயரிடு."
content_hash: 8ba8f867c3f9216c93054223e5a1fa013c932130
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mv.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mv.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mv.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mv

கோப்புகளையோ அடைவுகளையோ நகர்த்து அல்லது மறுபெயரிடு.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- கோப்பை ஓரிடத்திலிருந்து இன்னோரிடத்திற்கு நகர்த்து:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறி/பாதை</span>

- ஒரு கோப்பு அல்லது கோப்பகத்தை ஏற்கனவே உள்ள கோப்பகத்திற்கு நகர்த்தவும்:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இருக்கும்_கோப்பகம்/பாதை</span>

- கோப்பு பெயர்களை வைத்து, கோப்புகளை மற்றொரு கோப்பகத்திற்கு நகர்த்தவும்:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை1/பாதை மூலப்பாதை2/பாதை ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இலக்கு_கோப்பகம்/பாதை</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் உறுதிப்படுத்தாதே:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறி/பாதை</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் கோப்பு அனுமதிகளைப் பொருட்படுத்தாது உறுதிப்படுத்து:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறி/பாதை</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதாதே:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறி/பாதை</span>

- கோப்புகளை verbose நிலையில் நகர்த்து, நகர்த்தப்படும் கோப்புகள் பட்டியலிடப்படும்:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலம்/பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறி/பாதை</span>
