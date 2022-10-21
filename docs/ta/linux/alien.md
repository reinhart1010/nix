---
layout: page
title: linux/alien (தமிழ்)
description: "வெவ்வேறு நிறுவல் தொகுப்புகளை மற்ற வடிவங்களுக்கு மாற்றவும்."
content_hash: abc7c0cec9a816d8d2bb6f0ff9e02c36dfbdeefd
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># alien

வெவ்வேறு நிறுவல் தொகுப்புகளை மற்ற வடிவங்களுக்கு மாற்றவும்.
மேலும் விவரத்திற்கு: <https://manned.org/alien>.

- ஒரு குறிப்பிட்ட நிறுவல் கோப்பை டெபியன் வடிவத்திற்கு மாற்றவும் (`.deb` நீட்டிப்பு):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- குறிப்பிட்ட நிறுவல் கோப்பை Red Hat வடிவத்திற்கு மாற்றவும் (`.rpm` நீட்டிப்பு):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஒரு குறிப்பிட்ட நிறுவல் கோப்பை ஸ்லாக்வேர் நிறுவல் கோப்பாக மாற்றவும் (`.tgz` நீட்டிப்பு):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஒரு குறிப்பிட்ட நிறுவல் கோப்பை டெபியன் வடிவத்திற்கு மாற்றி கணினியில் நிறுவவும்:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>
