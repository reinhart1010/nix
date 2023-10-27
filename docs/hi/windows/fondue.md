---
layout: page
title: windows/fondue (हिन्दी)
description: "वैकल्पिक विंडोज़ सुविधाएँ स्थापित करें।"
content_hash: 74ed44b66acf78c060b3dcd9ff45649dbc87bed9
last_modified_at: 2023-10-25
related_topics:
  - title: English version
    url: /en/windows/fondue.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/fondue.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fondue

वैकल्पिक विंडोज़ सुविधाएँ स्थापित करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- एक विशिष्ट विंडोज़ सुविधा सक्षम करें:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशेषता</span>

- उपयोगकर्ता के लिए सभी आउटपुट संदेश छिपाएँ:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशेषता</span>` /hide-ux:all`

- त्रुटि रिपोर्टिंग के लिए कॉलर प्रक्रिया का नाम निर्दिष्ट करें:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">विशेषता</span>` /caller-name:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">नाम</span>