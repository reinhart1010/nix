---
layout: page
title: common/b2sum (தமிழ்)
description: "BLAKE2 மறையீட்டு சரிகாண்தொகைகளைக் கணி அல்லது சரிபார்."
content_hash: 7ef4c859f36f9dde20d474da24a37d2e4e621bb5
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/b2sum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/b2sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/b2sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/b2sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b2sum

BLAKE2 மறையீட்டு சரிகாண்தொகைகளைக் கணி அல்லது சரிபார்.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/b2sum>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளுக்கான BLAKE2 சரிகாண்தொகையைக் கணி:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>

- BLAKE2 சரிகாண்தொகை பட்டியலைக் கணக்கிட்டு ஒரு கோப்பில் சேமிக்கவும்:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.b2/பாதை</span>

- `stdin` (இயல் உள்ளீடு) இலிருந்து BLAKE2 சரிகாண்தொகையை கணி:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சில_கட்டளை</span>` | b2sum`

- BLAKE2 SHA1 தொகைகள் மற்றும் கோப்புப்பெயர்களின் கோப்பைப் படித்து, எல்லாக் கோப்புகளிலும் சரிகாண்தொகைகள் பொருந்துகின்றன என்பதைச் சரிபார்க்கவும்:

`b2sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.b2/பாதை</span>

- விடுபட்ட கோப்புகள் அல்லது சரிபார்ப்பு தோல்வியுற்றால் மட்டுமே செய்தியைக் காட்டவும்:

`b2sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.b2/பாதை</span>

- விடுபட்ட கோப்புகளைப் புறக்கணித்து, சரிபார்ப்பு தோல்வியுற்ற கோப்புகளுக்கான செய்தியை மட்டும் காட்டவும்:

`b2sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.b2/பாதை</span>
