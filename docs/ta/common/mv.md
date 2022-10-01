---
layout: page
title: common/mv (தமிழ்)
description: "கோப்புகளையோ அடைவுகளையோ நகர்த்து அல்லது மறுபெயரிடு."
content_hash: 1c6a7024747d391c1f6e40a0708796f4ff0470a4
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
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
---
# mv

கோப்புகளையோ அடைவுகளையோ நகர்த்து அல்லது மறுபெயரிடு.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/mv>.

- கோப்பை ஓரிடத்திலிருந்து இன்னோரிடத்திற்கு நகர்த்து:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிபாதை</span>

- கோப்பு பெயர்களை வைத்து, கோப்புகளை மற்றொரு கோப்பகத்திற்கு நகர்த்தவும்:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">இலக்கு_கோப்பகம்</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் உறுதிப்படுத்தாதே:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிபாதை</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் கோப்பு அனுமதிகளைப் பொருட்படுத்தாது உறுதிப்படுத்து:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிகோப்பு</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதாதே:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிகோப்பு</span>

- கோப்புகளை வளவள நிலையில் (நகர்த்தப்படும் கோப்புகள் பட்டியலிடப்படும்) நகர்த்து:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிகோப்பு</span>
