---
layout: page
title: linux/alien (தமிழ்)
description: "வெவ்வேறு நிறுவல் தொகுப்புகளை மற்ற வடிவங்களுக்கு மாற்றவும்."
content_hash: 095efbebcc1a3b9a783b95ea289a8c16a2abf7dc
last_modified_at: 2023-11-13
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alien

வெவ்வேறு நிறுவல் தொகுப்புகளை மற்ற வடிவங்களுக்கு மாற்றவும்.
மேலும் விவரத்திற்கு: <https://manned.org/alien>.

- ஒரு குறிப்பிட்ட நிறுவல் கோப்பை டெபியன் வடிவத்திற்கு மாற்றவும் (`.deb` நீட்டிப்பு):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- குறிப்பிட்ட நிறுவல் கோப்பை Red Hat வடிவத்திற்கு மாற்றவும் (`.rpm` நீட்டிப்பு):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- ஒரு குறிப்பிட்ட நிறுவல் கோப்பை ஸ்லாக்வேர் நிறுவல் கோப்பாக மாற்றவும் (`.tgz` நீட்டிப்பு):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- ஒரு குறிப்பிட்ட நிறுவல் கோப்பை டெபியன் வடிவத்திற்கு மாற்றி கணினியில் நிறுவவும்:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>
