---
layout: page
title: windows/ftp (हिन्दी)
description: "स्थानीय और दूरस्थ FTP सर्वर के बीच इंटरएक्टिव रूप से फ़ाइलें स्थानांतरित करें।"
content_hash: 4febd2b61a4b30536ba3463bb8f5d6057c8d092f
last_modified_at: 2024-11-27
related_topics:
  - title: Deutsch version
    url: /de/windows/ftp.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/ftp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ftp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/ftp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/ftp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

स्थानीय और दूरस्थ FTP सर्वर के बीच इंटरएक्टिव रूप से फ़ाइलें स्थानांतरित करें।
अधिक जानकारी: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>।

- एक दूरस्थ FTP सर्वर से इंटरएक्टिव रूप से कनेक्ट करें:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होस्ट</span>

- एक गुमनाम उपयोगकर्ता के रूप में लॉग इन करें:

`ftp -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होस्ट</span>

- प्रारंभिक कनेक्शन पर स्वचालित लॉगिन को निष्क्रिय करें:

`ftp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होस्ट</span>

- FTP कमांड की सूची वाली फ़ाइल चलाएँ:

`ftp -s:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल\का\पथ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">होस्ट</span>

- कई फ़ाइलें डाउनलोड करें (ग्लोब अभिव्यक्ति):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- कई फ़ाइलें अपलोड करें (ग्लोब अभिव्यक्ति):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- दूरस्थ सर्वर पर कई फ़ाइलें हटाएँ:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- मदद प्रदर्शित करें:

`ftp --help`
