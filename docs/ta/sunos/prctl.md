---
layout: page
title: sunos/prctl (தமிழ்)
description: "இயங்கும் செயல்முறைகளின், பணிகள் மற்றும் திட்டங்களின் ஆதாரக் கட்டுப்பாடு பெறவும் அல்லது அமைக்கவும்."
content_hash: 69553474aaf2cc2961574324f1d7021d9b5a58e7
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
---
# prctl

இயங்கும் செயல்முறைகளின், பணிகள் மற்றும் திட்டங்களின் ஆதாரக் கட்டுப்பாடு பெறவும் அல்லது அமைக்கவும்.
மேலும் விவரத்திற்கு: <https://www.unix.com/man-page/sunos/1/prctl>.

- செயல்முறை வரம்புகள் மற்றும் அனுமதிகளை ஆய்வு செய்:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- இயந்திர பாகுபடுத்தக்கூடிய வடிவத்தில் செயல்முறை வரம்புகள் மற்றும் அனுமதிகளை ஆய்வு செய்:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- இயங்கும் செயல்முறைக்கான குறிப்பிட்ட வரம்பைப் பெறுங்கள்:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>
