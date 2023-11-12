---
layout: page
title: linux/dnf (தமிழ்)
description: "RHEL, Fedora மற்றும் CentOS க்கான தொகுப்பு மேலாண்மை பயன்பாடு (yum ஐ மாற்றுகிறது)."
content_hash: 1f6e830ce05391002643baa7cf953e18d21b0382
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf

RHEL, Fedora மற்றும் CentOS க்கான தொகுப்பு மேலாண்மை பயன்பாடு (yum ஐ மாற்றுகிறது).
மேலும் விவரத்திற்கு: <https://dnf.readthedocs.io>.

- நிறுவப்பட்ட தொகுப்புகளை புதிய கிடைக்கக்கூடிய பதிப்புகளுக்கு மேம்படுத்தவும்:

`sudo dnf upgrade`

- முக்கிய வார்த்தைகள் மூலம் தொகுப்புகளைத் தேடுங்கள்:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">முக்கிய வார்த்தைகள்</span>

- தொகுப்பு பற்றிய விவரங்களைக் காண்பி:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- புதிய தொகுப்பை நிறுவவும் (அனைத்து அறிவுறுத்தல்களையும் தானாக உறுதிப்படுத்த `-y` ஐப் பயன்படுத்தவும்):

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- ஒரு தொகுப்பை அகற்று:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">நிரல்தொகுப்பு</span>

- நிறுவப்பட்ட தொகுப்புகளை பட்டியலிடுங்கள்:

`dnf list --installed`

- கொடுக்கப்பட்ட கோப்பை எந்த தொகுப்புகள் வழங்குகின்றன என்பதைக் கண்டறியவும்:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- அனைத்து கடந்த செயல்பாடுகளையும் காண்க:

`dnf history`
