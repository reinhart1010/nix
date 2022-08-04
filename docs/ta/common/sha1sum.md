---
layout: page
title: common/sha1sum (தமிழ்)
description: "SHA1 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: 5494ad464bce9d54ca572d097c4ef9fccd6cfd1b
related_topics:
  - title: English version
    url: /en/common/sha1sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha1sum.html
    icon: bi bi-globe
---
# sha1sum

SHA1 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/sha1sum>.

- கோப்பின் SHA1 சரிகாண்தொகையைக் கணி:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- பலக் கோப்புகளின் SHA1 சரிகாண்தொகையைக் கணி:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>

- SHA1 சரிகாண்தொகைகளைக் கணித்து கோப்பில் எழுது:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha1</span>

- SHA1 சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`sha1sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha1</span>

- பிழையுற்ற கோப்புகளை மட்டும் காட்டு:

`sha1sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha1</span>
