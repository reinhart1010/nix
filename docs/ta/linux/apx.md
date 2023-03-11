---
layout: page
title: linux/apx (தமிழ்)
description: "தொகுப்பு மேலாண்மை பயன்பாடு."
content_hash: 5d4b2542ccd9b501f7a7f739eece05bc28451059
last_modified_at: 2023-03-11
related_topics:
  - title: English version
    url: /en/linux/apx.html
    icon: bi bi-globe
---
# apx

தொகுப்பு மேலாண்மை பயன்பாடு.
பல மூலங்களிலிருந்து நிர்வகிக்கப்பட்ட கொள்கலன்களுக்குள் தொகுப்புகளை நிறுவவும் (`apx` அனைத்து கட்டளைகளிலும் --aur,--dnf, --apk கொடிகளை ஆதரிக்கிறது).
மேலும் விவரத்திற்கு: <https://github.com/Vanilla-OS/apx>.

- ஒரு குறிப்பிட்ட கொள்கலனை துவக்கவும் அல்லது மீண்டும் துவக்கவும்:

`apx init`

- கொள்கலனில் குறிப்பிட்ட தொகுப்புகளை நிறுவவும்:

`apx install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு1 நிரல்தொகுப்பு2 ...</span>

- கொள்கலனுக்குள் DEB/RPM தொகுப்பை நிறுவவும் (RPMகளை நிறுவ `--dnf` கொடியைப் பயன்படுத்தவும்):

`apx install --sideload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/நிரல்தொகுப்பு</span>

- கொள்கலனில் இருந்து குறிப்பிட்ட தொகுப்புகளை அகற்றவும்:

`apx remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு1 நிரல்தொகுப்பு2 ...</span>

- குறிப்பிட்ட தொகுப்புகளுக்காக தேடவும்:

`apx search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு1 நிரல்தொகுப்பு2 ...</span>

- கட்டளைகளை இயக்க நிர்வகிக்கப்படும் கொள்கலன் ஷெல்லை (ஓடு) உள்ளிடவும் (கண்டெய்னரில் இருந்து வெளியேற `exit` என தட்டச்சு செய்யவும்):

`apx enter`

- கொள்கலனில் கிடைக்கும் தொகுப்புகளின் பட்டியலைப் புதுப்பிக்கவும்:

`apx update`

- கொள்கலனில் நிறுவப்பட்ட அனைத்து தொகுப்புகளையும் அவற்றின் புதிய கிடைக்கக்கூடிய பதிப்பிற்கு மேம்படுத்தவும்:

`apx upgrade`
