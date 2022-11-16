---
layout: page
title: common/vt (தமிழ்)
description: "வைரஸ் டோட்டலுக்கான கட்டளை-வரி இடைமுகம்."
content_hash: f648091c8ff21c9ada8a5a7b6f94f7df9141a5da
related_topics:
  - title: English version
    url: /en/common/vt.html
    icon: bi bi-globe
---
# vt

வைரஸ் டோட்டலுக்கான கட்டளை-வரி இடைமுகம்.
இந்த கட்டளைக்கு வைரஸ் டோட்டல் கணக்கிலிருந்து API விசை தேவை.
மேலும் விவரத்திற்கு: <https://github.com/VirusTotal/vt-cli>.

- வைரஸ்களுக்காக ஒரு குறிப்பிட்ட கோப்பை ஸ்கேன் செய்யவும்:

`vt scan file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- வைரஸ்களுக்காக URL ஐ ஸ்கேன் செய்யவும்:

`vt scan url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- ஒரு குறிப்பிட்ட பகுப்பாய்விலிருந்து தகவலைக் காண்பி:

`vt analysis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_ஐடி|பகுப்பாய்வு_ஐடி</span>

- என்க்ரிப்ட் செய்யப்பட்ட `.zip` வடிவத்தில் கோப்புகளைப் பதிவிறக்கவும் (பிரீமியம் கணக்கு தேவை):

`vt download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு_ஐடி</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">அடைவிற்குப்/பாதை</span>` --zip --zip-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கடவுச்சொல்</span>

- ஊடாடும் வகையில் API விசையை உள்ளிட `vt` ஐத் துவக்கவும் அல்லது மீண்டும் தொடங்கவும்:

`vt init`

- ஒரு டொமைன் பற்றிய தகவலைக் காட்டு:

`vt domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- குறிப்பிட்ட URLக்கான தகவலைக் காட்டு:

`vt url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- குறிப்பிட்ட IP(ஐபி) முகவரிக்கான தகவலைக் காண்பி:

`vt domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ஐபி_முகவரி</span>
