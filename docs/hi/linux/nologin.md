---
layout: page
title: linux/nologin (हिन्दी)
description: "उपयोक्ता को लॉग इन करने से रोकने वाला वैकल्पिक शैल."
content_hash: 62bac20f74df996db05982ac06ba13d469717306
last_modified_at: 2023-11-02
related_topics:
  - title: Deutsch version
    url: /de/linux/nologin.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/nologin.html
    icon: bi bi-globe
---
# nologin

उपयोक्ता को लॉग इन करने से रोकने वाला वैकल्पिक शैल.
अधिक जानकारी: <https://manned.org/nologin.5>।

- उपयोक्ता को लॉग इन करने से रोकने के लिए उपयोक्ता की लॉगिन शैल को 'नोलॉगिन' पर सेट करें:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता</span>` nologin`

- नोलॉगिन लॉगिन शैल वाले उपयोक्ताओं के लिए संविभिन्न संदेश का अनुकूलन करें:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">अस्वीकृत_लॉगिन_संदेश</span>`" > /etc/nologin.txt`
