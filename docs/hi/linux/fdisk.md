---
layout: page
title: linux/fdisk (हिन्दी)
description: "एक प्रोग्राम जो हार्ड डिस्क पर पार्टीशन टेबल और पार्टीशन का प्रबंधन करने के लिए है।"
content_hash: a8e1481a826c6af53c94ecb1a87ad9e557cb0678
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/linux/fdisk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fdisk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/fdisk.html
    icon: bi bi-globe
---
# fdisk

एक प्रोग्राम जो हार्ड डिस्क पर पार्टीशन टेबल और पार्टीशन का प्रबंधन करने के लिए है।
देखें भी: `partprobe`.
अधिक जानकारी: <https://manned.org/fdisk>।

- पार्टीशनों की सूची दिखाएं:

`sudo fdisk -l`

- पार्टीशन मैनिपुलेटर शुरू करें:

`sudo fdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- एक डिस्क को पार्टीशन करते समय, एक पार्टीशन बनाएं:

`n`

- एक डिस्क को पार्टीशन करते समय, डिलीट करने के लिए एक पार्टीशन का चयन करें:

`d`

- एक डिस्क को पार्टीशन करते समय, पार्टीशन टेबल देखें:

`p`

- एक डिस्क को पार्टीशन करते समय, की गई परिवर्तनों को लिखें:

`w`

- एक डिस्क को पार्टीशन करते समय, की गई परिवर्तनों को छोड़ दें:

`q`

- एक डिस्क को पार्टीशन करते समय, हेल्प मेनू खोलें:

`m`
