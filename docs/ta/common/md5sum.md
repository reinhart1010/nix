---
layout: page
title: common/md5sum (தமிழ்)
description: "MD5 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: 291d9ca171332ade00dbf18de723d6e25b6a4a3a
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

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- பலக் கோப்புகளின் MD5 சரிகாண்தொகையைக் கணி:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு2</span>

- இயல் உள்ளீட்டின் MD5 சரிகாண்தொகையைக் கணி:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">உரை</span>`" | md5sum`

- MD5SUMகளின் கோப்பைப் படித்து, எல்லா கோப்புகளிலும் சரிகாண்தொகை பொருந்துகின்றனவா என்பதைச் சரிபார்க்கவும்:

`md5sum --check  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.md5</span>

- விடுபட்ட கோப்புகள் அல்லது சரிபார்ப்பு தோல்வியுற்றால் மட்டுமே செய்தியைக் காட்டவும்:

`md5sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.md5</span>

- விடுபட்ட கோப்புகளைப் புறக்கணித்து, சரிபார்ப்பு தோல்வியுற்ற கோப்புகளுக்கான செய்தியை மட்டும் காட்டவும்:

`md5sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.md5</span>
