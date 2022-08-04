---
layout: page
title: common/sha384sum (தமிழ்)
description: "SHA384 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: cb9bb28473dca8b95875312df72ce9b6ef7a3aad
related_topics:
  - title: English version
    url: /en/common/sha384sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha384sum.html
    icon: bi bi-globe
---
# sha384sum

SHA384 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- கோப்பின் SHA384 சரிகாண்தொகையைக் கணி:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- பலக் கோப்புகளின் SHA384 சரிகாண்தொகையைக் கணி:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>

- SHA384 சரிகாண்தொகைகளைக் கணித்து கோப்பில் எழுது:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha384</span>

- SHA384 சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`sha384sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha384</span>

- பிழையுற்ற கோப்புகளை மட்டும் காட்டு:

`sha384sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha384</span>
