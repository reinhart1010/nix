---
layout: page
title: linux/systemctl (हिन्दी)
description: "systemd सिस्टम और सेवा प्रबंधक को नियंत्रित करें।"
content_hash: 077d5484f46a817f3ab3924669ce322eeab6c287
last_modified_at: 2023-11-06
related_topics:
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/systemctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/systemctl.html
    icon: bi bi-globe
---
# systemctl

systemd सिस्टम और सेवा प्रबंधक को नियंत्रित करें।
अधिक जानकारी: <https://www.freedesktop.org/software/systemd/man/systemctl.html>।

- सभी चल रही सेवाएँ दिखाएं:

`systemctl status`

- विफल इकाइयों की सूची:

`systemctl --failed`

- सेवा को चालना/रोकना/पुनरारंभ करना/रीलोड करना:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इकाई</span>

- एक इकाई की स्थिति दिखाएं:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इकाई</span>

- एक इकाई को बूटअप पर स्वचलित रूप से चालाने/रोकने के लिए सक्षम/अक्षम करें:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इकाई</span>

- एक इकाई को सक्षम/अक्षम करने और मैन्युअल सक्रियण से रोकने/हटाने के लिए मास्क/अनमास्क करें:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इकाई</span>

- systemd को पुनः लोड करें, नई या बदली गई इकाइयों के लिए स्कैन करें:

`systemctl daemon-reload`

- क्या किसी इकाई को सक्षम किया गया है, यह जाँचें:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">इकाई</span>
