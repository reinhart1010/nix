---
layout: page
title: common/b2sum (தமிழ்)
description: "BLAKE2 கிரிப்டோகிராஃபிக் செக்ஸம்களைக் கணக்கிடவும்."
content_hash: f1e7c9769bf49699d9fec1336d883b2f6fd71e15
last_modified_at: 2023-11-12
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

BLAKE2 கிரிப்டோகிராஃபிக் செக்ஸம்களைக் கணக்கிடவும்.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/b2sum>.

- ஒரு கோப்பிற்கான BLAKE2 செக்சம் கணக்கிடவும்:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- பல கோப்புகளுக்கான BLAKE2 செக்சம்களைக் கணக்கிடவும்:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு2</span>

- `stdin` இலிருந்து BLAKE2 செக்சம் கணக்கிடவும்:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">சில_கட்டளை</span>` | b2sum`

- BLAKE2 தொகைகள் மற்றும் கோப்புப்பெயர்களின் கோப்பைப் படித்து, எல்லா கோப்புகளிலும் செக்சம்கள் பொருந்துகின்றன என்பதைச் சரிபார்க்கவும்:

`b2sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.b2</span>

- விடுபட்ட கோப்புகள் அல்லது சரிபார்ப்பு தோல்வியுற்றால் மட்டுமே செய்தியைக் காட்டவும்:

`b2sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.b2</span>

- விடுபட்ட கோப்புகளைப் புறக்கணித்து, சரிபார்ப்பு தோல்வியுற்ற கோப்புகளுக்கான செய்தியை மட்டும் காட்டவும்:

`b2sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.b2</span>
