---
layout: page
title: linux/apache2ctl (हिन्दी)
description: "अपाचे HTTP वेब सर्वर का प्रबंधन करें।"
content_hash: bd37210e833fb6be6f44413024b6a3a4ee80bfb2
last_modified_at: 2023-11-04
related_topics:
  - title: Deutsch version
    url: /de/linux/apache2ctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apache2ctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
---
# apache2ctl

अपाचे HTTP वेब सर्वर का प्रबंधन करें।
यह कमांड डेबियन आधारित ओएस के साथ आता है, आरएचईएल आधारित ओएस के लिए `httpd` देखें।
अधिक जानकारी: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- अपाचे डेमॉन प्रारंभ करें. यदि संदेश पहले से चल रहा हो तो उसे फेंकें:

`sudo apache2ctl start`

- अपाचे डेमॉन बंद करो:

`sudo apache2ctl stop`

- अपाचे डेमॉन को पुनरारंभ करें:

`sudo apache2ctl restart`

- कॉन्फ़िगरेशन फ़ाइल के सिंटैक्स का परीक्षण करें:

`sudo apache2ctl -t`

- लोड किए गए मॉड्यूल की सूची बनाएं:

`sudo apache2ctl -M`
