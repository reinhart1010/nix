---
layout: page
title: common/ssh (हिन्दी)
description: "सिक्योर शेल एक प्रोटोकॉल है जिसका उपयोग रिमोट सिस्टम पर सुरक्षित रूप से लॉग ऑन करने के लिए किया जाता है।"
content_hash: cda4cde5bb986c3fc17a5f01244ba072cafa7446
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ssh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ssh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh

सिक्योर शेल एक प्रोटोकॉल है जिसका उपयोग रिमोट सिस्टम पर सुरक्षित रूप से लॉग ऑन करने के लिए किया जाता है।
इसका उपयोग रिमोट सर्वर पर लॉगिंग या कमांड निष्पादित करने के लिए किया जा सकता है।
अधिक जानकारी: <https://man.openbsd.org/ssh>।

- रिमोट सर्वर से कनेक्ट करें:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>

- एक विशिष्ट पहचान (निजी कुंजी) के साथ एक दूरस्थ सर्वर से कनेक्ट करें:

`ssh -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/स्थान</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>

- किसी विशिष्ट पोर्ट का उपयोग करके किसी दूरस्थ सर्वर से कनेक्ट करें:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2222</span>

- रिमोट सर्वर पर [t] ty आवंटन के साथ एक कमांड चलाएँ जो रिमोट कमांड के साथ इंटरेक्शन की अनुमति देता है:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कमांड</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">कमांड_विकल्प</span>

- SSH टनलिंग: डायनेमिक पोर्ट फ़ॉरवर्डिंग (`लोकलहोस्ट: 1080 पर SOCKS प्रॉक्सी):

`ssh -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>

- एसएसएच टनलिंग: एक विशिष्ट पोर्ट (`लोकलहोस्ट: 9999` से `example.org:80`) को अग्रेषित करें, साथ ही छद्म-[टी] ty आवंटन और रिमोट कमांड के निष्पादन [एन] को अक्षम करने के साथ:

`ssh -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9999</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -N -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>

- SSH जंपिंग: एक जम्पहोस्ट के माध्यम से एक दूरस्थ सर्वर से कनेक्ट करें (कई जंप हॉप्स को अल्पविराम वर्णों से अलग करके निर्दिष्ट किया जा सकता है):

`ssh -J `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">जंप_होस्ट</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>

- एजेंट अग्रेषण: रिमोट मशीन को प्रमाणीकरण जानकारी अग्रेषित करें (उपलब्ध विकल्पों के लिए `man ssh_config` देखें):

`ssh -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>
