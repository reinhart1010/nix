---
layout: page
title: windows/netstat (हिन्दी)
description: "सक्रिय TCP कनेक्शनों, उन पोर्टों को प्रदर्शित करें जिन पर कंप्यूटर सुन रहा है, नेटवर्क एडाप्टर के आँकड़े, IP रूटिंग टेबल, IPv4 आँकड़े और IPv6 आँकड़े।"
content_hash: 625013c81cb5ded034c281f773d3025d0dc25958
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/windows/netstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/netstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

सक्रिय TCP कनेक्शनों, उन पोर्टों को प्रदर्शित करें जिन पर कंप्यूटर सुन रहा है, नेटवर्क एडाप्टर के आँकड़े, IP रूटिंग टेबल, IPv4 आँकड़े और IPv6 आँकड़े।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>।

- सक्रिय TCP कनेक्शनों को प्रदर्शित करें:

`netstat`

- सभी सक्रिय TCP कनेक्शनों और TCP और UDP पोर्टों को प्रदर्शित करें जिन पर कंप्यूटर सुन रहा है:

`netstat -a`

- नेटवर्क एडाप्टर के आँकड़े प्रदर्शित करें, जैसे भेजे गए और प्राप्त किए गए बाइट्स और पैकेट्स की संख्या:

`netstat -e`

- सक्रिय TCP कनेक्शनों को प्रदर्शित करें और पतों और पोर्ट नंबरों को संख्यात्मक रूप में व्यक्त करें:

`netstat -n`

- सक्रिय TCP कनेक्शनों को प्रदर्शित करें और प्रत्येक कनेक्शन के लिए प्रक्रिया आईडी (PID) शामिल करें:

`netstat -o`

- IP रूटिंग टेबल की सामग्री प्रदर्शित करें:

`netstat -r`

- प्रोटोकॉल द्वारा आँकड़े प्रदर्शित करें:

`netstat -s`

- वर्तमान में खुले पोर्टों और संबंधित IP पतों की सूची प्रदर्शित करें:

`netstat -an`
