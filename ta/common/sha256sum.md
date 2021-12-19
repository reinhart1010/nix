---
layout: page
title: common/sha256sum (தமிழ்)
description: "SHA256 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: 586317a2702aedc023cb443e1441055095db528b
related_topics:
  - title: English version
    url: /en/common/sha256sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha256sum.html
    icon: bi bi-globe
---
# sha256sum

SHA256 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- கோப்பின் SHA256 சரிகாண்தொகையைக் கணி:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- பலக் கோப்புகளின் SHA256 சரிகாண்தொகையைக் கணி:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>

- SHA256 சரிகாண்தொகைகளைக் கணித்து கோப்பில் எழுது:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha256</span>

- SHA256 சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`sha256sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha256</span>

- பிழையுற்ற கோப்புகளை மட்டும் காட்டு:

`sha256sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha256</span>
