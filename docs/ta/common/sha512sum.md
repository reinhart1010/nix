---
layout: page
title: common/sha512sum (தமிழ்)
description: "SHA512 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: c44dda38f75b438ec024da864da43ed770157e74
related_topics:
  - title: English version
    url: /en/common/sha512sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha512sum.html
    icon: bi bi-globe
---
# sha512sum

SHA512 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- கோப்பின் SHA512 சரிகாண்தொகையைக் கணி:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- பலக் கோப்புகளின் SHA512 சரிகாண்தொகையைக் கணி:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>

- SHA512 சரிகாண்தொகைகளைக் கணித்து கோப்பில் எழுது:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha512</span>

- SHA512 சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`sha512sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha512</span>

- பிழையுற்ற கோப்புகளை மட்டும் காட்டு:

`sha512sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha512</span>
