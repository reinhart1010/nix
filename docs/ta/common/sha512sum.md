---
layout: page
title: common/sha512sum (தமிழ்)
description: "SHA512 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: 54b436d25394a62c07db0e2a08570b1729443e61
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/sha512sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sha512sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sha512sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha512sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha512sum

SHA512 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளுக்கான SHA512 சரிகாண்தொகையைக் கணி:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>

- SHA512 சரிகாண்தொகை பட்டியலைக் கணக்கிட்டு ஒரு கோப்பில் சேமிக்கவும்:

`sha512sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha512/பாதை</span>

- `stdin` (இயல் உள்ளீடு) இலிருந்து SHA512 சரிகாண்தொகையை கணி:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>` | sha512sum`

- SHA512 தொகைகள் மற்றும் கோப்புப்பெயர்களின் கோப்பைப் படித்து, எல்லாக் கோப்புகளிலும் சரிகாண்தொகைகள் பொருந்துகின்றன என்பதைச் சரிபார்க்கவும்:

`sha512sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha512/பாதை</span>

- விடுபட்ட கோப்புகள் அல்லது சரிபார்ப்பு தோல்வியுற்றால் மட்டுமே செய்தியைக் காட்டவும்:

`sha512sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha512/பாதை</span>

- சரிபார்ப்பு தோல்வியுற்றால், விடுபட்ட கோப்புகளைப் புறக்கணித்து, செய்தியை மட்டும் காட்டவும்:

`sha512sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha512/பாதை</span>
