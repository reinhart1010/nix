---
layout: page
title: common/mv (தமிழ்)
description: "கோப்புகளையோ அடைவுகளையோ நகர்த்து அல்லது மறுபெயரிடு."
content_hash: 746c7b5ec44d32fa215a6c79b74571f3c4ef46d8
last_modified_at: 2023-05-24
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

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mv

கோப்புகளையோ அடைவுகளையோ நகர்த்து அல்லது மறுபெயரிடு.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/mv>.

- கோப்பை ஓரிடத்திலிருந்து இன்னோரிடத்திற்கு நகர்த்து:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூலம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/குறி</span>

- ஒரு கோப்பு அல்லது கோப்பகத்தை ஏற்கனவே உள்ள கோப்பகத்திற்கு நகர்த்தவும்:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூலம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/இருக்கும்_கோப்பகம்</span>

- கோப்பு பெயர்களை வைத்து, கோப்புகளை மற்றொரு கோப்பகத்திற்கு நகர்த்தவும்:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூலப்பாதை1 பாதை/டு/மூலப்பாதை2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/இலக்கு_கோப்பகம்</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் உறுதிப்படுத்தாதே:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூலம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/குறி</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் கோப்பு அனுமதிகளைப் பொருட்படுத்தாது உறுதிப்படுத்து:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூலம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/குறி</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதாதே:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூலம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/குறி</span>

- கோப்புகளை verbose நிலையில் நகர்த்து, நகர்த்தப்படும் கோப்புகள் பட்டியலிடப்படும்:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/மூலம்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/குறி</span>
