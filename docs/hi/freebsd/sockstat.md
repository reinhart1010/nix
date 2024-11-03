---
layout: page
title: freebsd/sockstat (हिन्दी)
description: "खुले इंटरनेट या UNIX डोमेन सॉकेट्स की सूची।"
content_hash: 8f6dcaf69e996cb43efa6456872620d3dc031c64
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/freebsd/sockstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/sockstat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

खुले इंटरनेट या UNIX डोमेन सॉकेट्स की सूची।
अधिक जानकारी: <https://man.freebsd.org/cgi/man.cgi?sockstat>।

- देखें कि कौन से उपयोगकर्ता/प्रक्रियाएँ किन पोर्ट्स पर [l]सुन रही हैं:

`sockstat -l`

- विशेष [p]पोर्ट्स पर विशेष [P]प्रोटोकॉल का उपयोग करते हुए IPv[4]/IPv[6] सॉकेट्स [l]सुनने की जानकारी दिखाएं:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- [c]कनेक्टेड सॉकेट्स भी दिखाएं, [n]संख्यात्मक UID को उपयोगकर्ता नाम में परिवर्तित न करें और [w]चौड़ी फ़ील्ड आकार का उपयोग करें:

`sockstat -cnw`

- केवल एक विशेष [j]जेल ID या नाम से संबंधित सॉकेट्स दिखाएं [v]विस्तृत मोड में:

`sockstat -jv`

- प्रोटोकॉल [s]राज्य और दूरस्थ [U]DP एनकैप्सुलेशन पोर्ट नंबर दिखाएं, यदि लागू हो (ये वर्तमान में केवल SCTP और TCP के लिए लागू हैं):

`sockstat -sU`

- प्रोटोकॉल [S]स्टैक और [C]कंजेशन कंट्रोल मॉड्यूल दिखाएं, यदि लागू हो (ये वर्तमान में केवल TCP के लिए लागू हैं):

`sockstat -CS`

- केवल इंटरनेट सॉकेट्स दिखाएं यदि स्थानीय और विदेशी पते लूपबैक नेटवर्क प्रीफिक्स 127.0.0.0/8 में नहीं हैं, या IPv6 लूपबैक पते ::1 को शामिल नहीं करते हैं:

`sockstat -L`

- हेडर न दिखाएं ([q]शांत मोड), [u]यूनिक्स सॉकेट्स दिखाएं और `inp_gencnt` प्रदर्शित करें:

`sockstat -qui`
