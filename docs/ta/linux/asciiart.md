---
layout: page
title: linux/asciiart (தமிழ்)
description: "படங்களை ASCII ஆக மாற்றவும்."
content_hash: c6eaed0291d0fcb022d9f07b710fce18b291ae04
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/asciiart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/asciiart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/asciiart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/asciiart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/asciiart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciiart

படங்களை ASCII ஆக மாற்றவும்.
மேலும் விவரத்திற்கு: <https://github.com/nodanaonlyzuul/asciiart>.

- ஒரு கோப்பிலிருந்து ஒரு படத்தைப் படித்து ASCII இல் அச்சிடவும்:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/படம்.jpg</span>

- URL இலிருந்து ஒரு படத்தைப் படித்து, ASCII இல் அச்சிடவும்:

`asciiart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com/image.jpg</span>

- வெளியீட்டு அகலத்தைத் தேர்வு செய்யவும் (இயல்புநிலை 100):

`asciiart --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/படம்.jpg</span>

- ASCII வெளியீட்டை வண்ணமயமாக்கவும்:

`asciiart --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/படம்.jpg</span>

- வெளியீட்டு வடிவமைப்பைத் தேர்வு செய்யவும் (இயல்புநிலை வடிவம் உரை):

`asciiart --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/படம்.jpg</span>

- எழுத்து வரைபடத்தைத் தலைகீழாக மாற்றவும்:

`asciiart --invert-chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/படம்.jpg</span>
