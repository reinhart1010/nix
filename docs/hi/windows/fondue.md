---
layout: page
title: windows/fondue (हिन्दी)
description: "वैकल्पिक विंडोज़ सुविधाएँ स्थापित करें।"
content_hash: dc0405687d7d8dff75307de6f144fb98deb286c6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/fondue.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/fondue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fondue

वैकल्पिक विंडोज़ सुविधाएँ स्थापित करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>।

- एक विशिष्ट विंडोज़ सुविधा सक्षम करें:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशेषता</span>

- उपयोगकर्ता के लिए सभी आउटपुट संदेश छिपाएँ:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशेषता</span>` /hide-ux:all`

- त्रुटि रिपोर्टिंग के लिए कॉलर प्रक्रिया का नाम निर्दिष्ट करें:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशेषता</span>` /caller-name:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>
