---
layout: page
title: common/mv (தமிழ்)
description: "கோப்புகளையோ அடைவுகளையோ நகர்த்து அல்லது மறுபெயரிடு."
content_hash: 3f5e3eaa65a35cdeaf9567c3fd381f14a5f8a6f7
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

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிபாதை</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் உறுதிப்படுத்தாதே:

`mv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலப்பாதை</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிபாதை</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதும் முன் கோப்பு அனுமதிகளைப் பொருட்படுத்தாது உறுதிப்படுத்து:

`mv -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிகோப்பு</span>

- ஏற்கனவே இருக்கும் கோப்புகள் மேலெழுதாதே:

`mv -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிகோப்பு</span>

- கோப்புகளை வளவள நிலையில் (நகர்த்தப்படும் கோப்புகள் பட்டியலிடப்படும்) நகர்த்து:

`mv -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">மூலக்கோப்பு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">குறிகோப்பு</span>
