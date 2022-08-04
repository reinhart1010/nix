---
layout: page
title: common/md5sum (தமிழ்)
description: "MD5 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: 82fe13181030c6afdc76415d3f9f69b6f427f59b
related_topics:
  - title: English version
    url: /en/common/md5sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/md5sum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/md5sum.html
    icon: bi bi-globe
---
# md5sum

MD5 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/md5sum>.

- கோப்பின் MD5 சரிகாண்தொகையைக் கணி:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- பலக் கோப்புகளின் MD5 சரிகாண்தொகையைக் கணி:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>

- MD5 சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`md5sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.md5</span>

- இயல் உள்ளீட்டின் MD5 சரிகாண்தொகையைக் கணி:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">உரை</span>`" | md5sum`
