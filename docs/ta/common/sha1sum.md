---
layout: page
title: common/sha1sum (தமிழ்)
description: "SHA1 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: f22880903a26093aa16989cac7df8ce3126b3352
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/sha1sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sha1sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sha1sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha1sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sha1sum

SHA1 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/sha1sum>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளுக்கான SHA1 சரிகாண்தொகையைக் கணி:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>

- SHA1 சரிகாண்தொகை பட்டியலைக் கணக்கிட்டு ஒரு கோப்பில் சேமிக்கவும்:

`sha1sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha1/பாதை</span>

- `stdin` (இயல் உள்ளீடு) இலிருந்து SHA1 சரிகாண்தொகையை கணி:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>` | sha1sum`

- SHA1 தொகைகள் மற்றும் கோப்புப்பெயர்களின் கோப்பைப் படித்து, எல்லாக் கோப்புகளிலும் சரிகாண்தொகைகள் பொருந்துகின்றன என்பதைச் சரிபார்க்கவும்:

`sha1sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha1/பாதை</span>

- விடுபட்ட கோப்புகள் அல்லது சரிபார்ப்பு தோல்வியுற்றால் மட்டுமே செய்தியைக் காட்டவும்:

`sha1sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha1/பாதை</span>

- சரிபார்ப்பு தோல்வியுற்றால், விடுபட்ட கோப்புகளைப் புறக்கணித்து, செய்தியை மட்டும் காட்டவும்:

`sha1sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha1/பாதை</span>
