---
layout: page
title: linux/cat (हिन्दी)
description: "फ़ाइलों को प्रिंट करता है और जोड़ता है।"
content_hash: 6f8174152390e922228d50ed8f023c8f7d16ed67
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/linux/cat.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

फ़ाइलों को प्रिंट करता है और जोड़ता है।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/cat>।

- फ़ाइल की सामग्री को मानक (standard) आउटपुट पर प्रिंट करें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक आउटपुट फ़ाइल में कई फ़ाइलों को सम्‍मिलित करें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल1/का/पथ फ़ाइल2/का/पथ ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फ़ाइल/का/पथ</span>

- आउटपुट फ़ाइल में कई फ़ाइलें जोड़ें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल1/का/पथ फ़ाइल2/का/पथ ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फ़ाइल/का/पथ</span>

- फ़ाइल में `stdin` लिखें:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- संख्या ([n]umber) सभी आउटपुट लाइनें:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- गैर-मुद्रण योग्य और खाली स्थान वाले वर्ण प्रदर्शित करें (`M-` उपसर्ग के साथ यदि गैर-ASCII है):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>
