---
layout: page
title: common/sha224sum (தமிழ்)
description: "SHA224 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: f8f96da2d981e20fdc2c81075549615c90779380
related_topics:
  - title: English version
    url: /en/common/sha224sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha224sum.html
    icon: bi bi-globe
---
# sha224sum

SHA224 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- கோப்பின் SHA224 சரிகாண்தொகையைக் கணி:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- பலக் கோப்புகளின் SHA224 சரிகாண்தொகையைக் கணி:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>

- SHA224 சரிகாண்தொகைகளைக் கணித்து கோப்பில் எழுது:

`sha224sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha224</span>

- SHA224 சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`sha224sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha224</span>

- பிழையுற்ற கோப்புகளை மட்டும் காட்டு:

`sha224sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha224</span>
