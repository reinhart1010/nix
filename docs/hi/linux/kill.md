---
layout: page
title: linux/kill (हिन्दी)
description: "एक प्रोग्राम को एक सिग्नल भेजता है, जो आमतौर पर प्रोग्राम को रोकने से संबंधित होता है।"
content_hash: 7083f1eb396ca513c11b5311512a6bc73e22a409
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/linux/kill.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kill

एक प्रोग्राम को एक सिग्नल भेजता है, जो आमतौर पर प्रोग्राम को रोकने से संबंधित होता है।
SIGKILL और SIGSTOP को छोड़कर सभी सिग्नल्स को प्रोग्राम द्वारा इंटरसेप्ट किया जा सकता है ताकि यह साफ-सुथरे तरीके से बाहर निकल सके।
अधिक जानकारी: <https://manned.org/kill>।

- डिफ़ॉल्ट SIGTERM (terminate) सिग्नल का उपयोग करके एक प्रोग्राम को समाप्त करें:

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रक्रिया_आईडी</span>

- सिग्नल मान और उनके संबंधित नामों की सूची दिखाएं (बिना `SIG` उपसर्ग के उपयोग किया जाता है):

`kill -L`

- एक बैकग्राउंड जॉब को समाप्त करें:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">जॉब_आईडी</span>

- SIGHUP (hang up) सिग्नल का उपयोग करके एक प्रोग्राम को समाप्त करें। कई डेमॉन प्रोग्राम समाप्त होने के बजाय पुनः लोड होंगे:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रक्रिया_आईडी</span>

- SIGINT (interrupt) सिग्नल का उपयोग करके एक प्रोग्राम को समाप्त करें। इसे आमतौर पर उपयोगकर्ता `Ctrl + C` दबाकर आरंभ करते हैं:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रक्रिया_आईडी</span>

- ऑपरेटिंग सिस्टम को सिग्नल भेजकर एक प्रोग्राम को तुरंत समाप्त करें (जिसे सिग्नल को कैप्चर करने का कोई अवसर नहीं मिलता है):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रक्रिया_आईडी</span>

- ऑपरेटिंग सिस्टम को सिग्नल भेजकर एक प्रोग्राम को रोकें जब तक कि SIGCONT ("जारी रखें") सिग्नल प्राप्त न हो:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">प्रक्रिया_आईडी</span>

- दिए गए GID (समूह आईडी) वाले सभी प्रक्रियाओं को `SIGUSR1` सिग्नल भेजें:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">समूह_आईडी</span>
