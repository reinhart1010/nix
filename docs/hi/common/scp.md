---
layout: page
title: common/scp (हिन्दी)
description: "सुरक्षित प्रति।"
content_hash: c18f57664baa6dd0a2529f6b7f3e9d0190b8be39
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/scp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/scp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scp

सुरक्षित प्रति।
SSH पर सिक्योर कॉपी प्रोटोकॉल का उपयोग करके होस्ट के बीच फ़ाइलों की प्रतिलिपि बनाएँ।
अधिक जानकारी: <https://man.openbsd.org/scp>।

- स्थानीय फ़ाइल को दूरस्थ होस्ट पर कॉपी करें:

`scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लोकल_फ़ाइल/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_फ़ाइल/का/स्थान​</span>

- रिमोट होस्ट से कनेक्ट करते समय एक विशिष्ट पोर्ट का उपयोग करें:

`scp -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पोर्ट​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लोकल_फ़ाइल/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_फ़ाइल/का/स्थान​</span>

- किसी फ़ाइल को दूरस्थ होस्ट से स्थानीय निर्देशिका में कॉपी करें:

`scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_फ़ाइल/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लोकल_डाइरेक्टरी/का/स्थान​</span>

- किसी निर्देशिका की सामग्री को दूरस्थ होस्ट से स्थानीय निर्देशिका में पुन: कॉपी करें:

`scp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_डाइरेक्टरी/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लोकल_डाइरेक्टरी/का/स्थान​</span>

- स्थानीय होस्ट के माध्यम से स्थानांतरित होने वाले दो दूरस्थ होस्ट के बीच फ़ाइल की प्रतिलिपि बनाएँ:

`scp -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पेहला_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_फ़ाइल/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">दूस्रा_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_डाइरेक्टरी/का/स्थान​</span>

- दूरस्थ होस्ट से कनेक्ट करते समय एक विशिष्ट उपयोगकर्ता नाम का उपयोग करें:

`scp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लोकल_फ़ाइल/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_उपयोगकर्ता_नाम</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_डाइरेक्टरी/का/स्थान​</span>

- दूरस्थ होस्ट के साथ प्रमाणीकरण के लिए विशिष्ट ssh निजी कुंजी का उपयोग करें:

`scp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्राइवेट_"की"/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">लोकल_फ़ाइल/का/स्थान​</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">रिमोट_होस्ट</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/रिमोट_फ़ाइल/का/स्थान​</span>
