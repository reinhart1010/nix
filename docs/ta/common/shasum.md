---
layout: page
title: common/shasum (தமிழ்)
description: "SHA மறையீட்டு சரிகாண்தொகைகளைக் கணி அல்லது சரிபார்."
content_hash: 8773e0bd0488d8575c93bcfbfd54f5f750eb4741
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/shasum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/shasum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shasum

SHA மறையீட்டு சரிகாண்தொகைகளைக் கணி அல்லது சரிபார்.
மேலும் விவரத்திற்கு: <https://manned.org/shasum>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளுக்கான SHA1 சரிகாண்தொகையைக் கணி:

`shasum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>

- ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளுக்கான SHA256 சரிகாண்தொகையைக் கணி:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>

- ஒன்று அல்லது அதற்கு மேற்பட்ட கோப்புகளுக்கான SHA512 சரிகாண்தொகைகளைக் கணி:

`shasum --algorithm 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>

- `stdin` (இயல் உள்ளீடு) இலிருந்து SHA1 சரிகாண்தொகையை கணி:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>` | shasum`

- SHA256 சரிகாண்தொகை பட்டியலைக் கணக்கிட்டு ஒரு கோப்பில் சேமிக்கவும்:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1/பாதை கோப்பு2/பாதை ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha256/பாதை</span>

- SHA1 தொகைகள் மற்றும் கோப்புப்பெயர்களின் கோப்பைப் படித்து, எல்லாக் கோப்புகளிலும் சரிகாண்தொகைகள் பொருந்துகின்றன என்பதைச் சரிபார்க்கவும்:

`shasum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- விடுபட்ட கோப்புகள் அல்லது சரிபார்ப்பு தோல்வியுற்றால் மட்டுமே செய்தியைக் காட்டவும்:

`shasum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>

- சரிபார்ப்பு தோல்வியுற்றால், விடுபட்ட கோப்புகளைப் புறக்கணித்து, செய்தியை மட்டும் காட்டவும்:

`shasum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு/பாதை</span>
