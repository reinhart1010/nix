---
layout: page
title: linux/brightnessctl (മലയാളം)
description: "മോണിറ്ററിന്റെ പ്രകാശതീവ്രത ലഭിക്കുവാനും നിയന്ത്രിക്കുവാനുമുള്ള ഗ്നു/ലിനക്സ് അധിഷ്ഠിത യൂട്ടിലിറ്റി."
content_hash: 566e81337609ee79aef18aa884008b2994a2ddae
related_topics:
  - title: English version
    url: /en/linux/brightnessctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brightnessctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brightnessctl

മോണിറ്ററിന്റെ പ്രകാശതീവ്രത ലഭിക്കുവാനും നിയന്ത്രിക്കുവാനുമുള്ള ഗ്നു/ലിനക്സ് അധിഷ്ഠിത യൂട്ടിലിറ്റി.
കൂടുതൽ വിവരങ്ങൾ: <https://github.com/Hummer12007/brightnessctl>.

- പ്രകാശം നിയന്ത്രിക്കാനാവുന്ന ഡിവൈസുകൾ കാണുവാൻ:

`brightnessctl --list`

- നിലവിലുള്ള പ്രകാശതീവ്രത അറിയുവാൻ:

`brightnessctl get`

- നിശ്ചിത ശതമാനത്തിലേക്ക് പ്രകാശതീവ്രത മാറ്റുവാൻ:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>

- നിലവിലെ പ്രകാശതീവ്രതയിലേക്കു നിശ്ചിത ശതമാനം കൂട്ടുവാൻ:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+10%</span>

- നിലവിലെ പ്രകാശതീവ്രതയിലേക്കു നിശ്ചിത ശതമാനം കുറയ്ക്കുവാൻ:

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
