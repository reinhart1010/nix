---
layout: page
title: linux/tshark (தமிழ்)
description: "பாக்கெட் பகுப்பாய்வு கருவி, வயர்ஷார்க்கின் CLI பதிப்பு."
content_hash: b872dbb8eae9753e99b190bc1310e2ec5697d654
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/tshark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tshark

பாக்கெட் பகுப்பாய்வு கருவி, வயர்ஷார்க்கின் CLI பதிப்பு.
மேலும் விவரத்திற்கு: <https://tshark.dev/>.

- லோக்கல் ஹோஸ்டில் அனைத்தையும் கண்காணிக்கவும்:

`tshark`

- குறிப்பிட்ட பிடிப்பு வடிப்பானுடன் பொருந்தும் பாக்கெட்டுகளை மட்டும் பிடிக்கவும்:

`tshark -f '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp port 53</span>`'`

- குறிப்பிட்ட வெளியீட்டு வடிப்பானுடன் பொருந்தும் பாக்கெட்டுகளை மட்டும் காட்டு:

`tshark -Y '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.request.method == "GET"</span>`'`

- ஒரு குறிப்பிட்ட நெறிமுறையைப் பயன்படுத்தி TCP போர்ட்டை டிகோட் செய்யவும் (எ.கா. HTTP):

`tshark -d tcp.port==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http</span>

- கைப்பற்றப்பட்ட வெளியீட்டின் வடிவமைப்பைக் குறிப்பிடவும்:

`tshark -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|text|ps|…</span>

- வெளியீட்டிற்கு குறிப்பிட்ட புலங்களைத் தேர்ந்தெடுக்கவும்:

`tshark -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fields|ek|json|pdml</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.request.method</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip.src</span>

- கைப்பற்றப்பட்ட பாக்கெட்டை ஒரு கோப்பில் எழுதவும்:

`tshark -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- ஒரு கோப்பிலிருந்து பாக்கெட்டுகளை பகுப்பாய்வு செய்யுங்கள்:

`tshark -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.pcap</span>
