---
layout: page
title: common/grep (தமிழ்)
description: "கோப்பில் தேடுகுறித்தொடர்களுடன் தேடு."
content_hash: c4edd3de426a24d52d03bc08ede75061c496fedb
last_modified_at: 2023-11-12
related_topics:
  - title: dansk version
    url: /da/common/grep.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/grep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/grep.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/grep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/grep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/grep.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/grep.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grep

கோப்பில் தேடுகுறித்தொடர்களுடன் தேடு.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/grep/manual/grep.html>.

- கோப்பில் தேடு:

`grep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடுதொடர்</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- தேடுகுறித்தொடரல்லா உருச்சரத்திற்குத் தேடு:

`grep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">உருச்சரம்</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- அடைவிலும் சேய் அடைவுகளிலுமுள்ள இருமக் கோப்பல்லா அனைத்துக் கோப்புகளையும் தேடு; பொருத்தங்களின் வரி எண்ணைக் காட்டு:

`grep --recursive --line-number --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடுதொடர்</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>

- எழுத்துயர்நிலை கருதாது விரிவுபட்ட தேடுகுறித்தொடர்களுடன் (`?`, `+`, `{}`, `|` ஆகியவற்றைப் பயன்படுத்தலாம்) தேடு:

`grep --extended-regexp --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடுதொடர்</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஒவ்வொருப் பொருத்தத்திற்கும் சூழ்ந்த, முந்தைய அல்லது பிந்தைய 3 வரிகளைக் காட்டு:

`grep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடுதொடர்</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஒவ்வொருப் பொருத்தத்திற்கும் கோப்புப் பெயரையும் வரி எண்ணையும் காட்டு:

`grep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடுதொடர்</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- தேடுதொடருக்குத் தேடு, ஆனால் பொருந்திய பகுதிகளை மட்டும் காட்டு:

`grep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடுதொடர்</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- இயல் உள்ளீட்டில் தேடுதொடருக்குப் பொருந்தா வரிகளை மட்டும் காட்டு:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>` | grep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">தேடுதொடர்</span>`"`
