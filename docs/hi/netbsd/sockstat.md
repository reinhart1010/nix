---
layout: page
title: netbsd/sockstat (हिन्दी)
description: "खुले इंटरनेट या UNIX डोमेन सॉकेट्स की सूची।"
content_hash: 1273bca8dcbca348a6b65055024a73d313d7abc1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/netbsd/sockstat.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/sockstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

खुले इंटरनेट या UNIX डोमेन सॉकेट्स की सूची।
नोट: यह प्रोग्राम FreeBSD के `sockstat` से NetBSD 3.0 के लिए एक पुनर्लेखन है।
देखें: `netstat`।
अधिक जानकारी: <https://man.netbsd.org/sockstat.1>।

- सुनने और जुड़े सॉकेट्स के लिए IPv4, IPv6 और यूनिक्स सॉकेट्स की जानकारी दिखाएँ:

`sockstat`

- एक विशिष्ट [p]पोर्ट पर एक विशिष्ट [P]प्रोटोकॉल का उपयोग करते हुए IPv[4]/IPv[6] सॉकेट्स [l]सुनने के लिए जानकारी दिखाएँ:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पोर्ट1,पोर्ट2...</span>

- [c]जुड़े सॉकेट्स भी दिखाएँ, [u]यूनिक्स सॉकेट्स दिखाते हुए:

`sockstat -cu`

- केवल [n]संख्यात्मक आउटपुट दिखाएँ, पते और पोर्ट्स के लिए प्रतीकात्मक नामों को हल किए बिना:

`sockstat -n`

- निर्दिष्ट पते के [f]परिवार के सॉकेट्स की केवल सूची बनाएं:

`sockstat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inet|inet6|local|unix</span>
