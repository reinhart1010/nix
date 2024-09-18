---
layout: page
title: linux/adduser (हिन्दी)
description: "उपयोगकर्ता जोड़ने की उपयोगिता।"
content_hash: 0c913d4ee9612c52761c1ff72905d05f9a37b392
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/adduser.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/adduser.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adduser

उपयोगकर्ता जोड़ने की उपयोगिता।
अधिक जानकारी: <https://manned.org/adduser>।

- डिफ़ॉल्ट होम निर्देशिका के साथ एक नया उपयोगकर्ता बनाएं और उपयोगकर्ता को पासवर्ड सेट करने के लिए संकेत दें:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- होम निर्देशिका के बिना एक नया उपयोगकर्ता बनाएँ:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- निर्दिष्ट पथ पर होम निर्देशिका के साथ एक नया उपयोगकर्ता बनाएँ:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होम/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- लॉगिन शेल के रूप में निर्दिष्ट शेल सेट के साथ एक नया उपयोगकर्ता बनाएँ:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">शेल/का/पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>

- निर्दिष्ट समूह से संबंधित कोई नया उपयोगकर्ता बनाएँ:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">समूह</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">उपयोगकर्ता_नाम</span>
