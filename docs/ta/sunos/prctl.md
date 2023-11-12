---
layout: page
title: sunos/prctl (தமிழ்)
description: "இயங்கும் செயல்முறைகளின், பணிகள் மற்றும் திட்டங்களின் ஆதாரக் கட்டுப்பாடு பெறவும் அல்லது அமைக்கவும்."
content_hash: cedd6471f33f1accb795cb297040852c18367a96
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prctl

இயங்கும் செயல்முறைகளின், பணிகள் மற்றும் திட்டங்களின் ஆதாரக் கட்டுப்பாடு பெறவும் அல்லது அமைக்கவும்.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/sunos/1/prctl>.

- செயல்முறை வரம்புகள் மற்றும் அனுமதிகளை ஆய்வு செய்:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- இயந்திர பாகுபடுத்தக்கூடிய வடிவத்தில் செயல்முறை வரம்புகள் மற்றும் அனுமதிகளை ஆய்வு செய்:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- இயங்கும் செயல்முறைக்கான குறிப்பிட்ட வரம்பைப் பெறுங்கள்:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
