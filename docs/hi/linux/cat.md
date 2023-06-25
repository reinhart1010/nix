---
layout: page
title: linux/cat (हिन्दी)
description: "फ़ाइलों को प्रिंट करता है और जोड़ता है।"
content_hash: 61f2b89461b654ae15b783140798ec41eae5fbe4
last_modified_at: 2023-06-16
related_topics:
  - title: English version
    url: /en/linux/cat.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/cat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cat

फ़ाइलों को प्रिंट करता है और जोड़ता है।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/cat>.

- फ़ाइल की सामग्री को मानक (standard) आउटपुट पर प्रिंट करें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- एक आउटपुट फ़ाइल में कई फ़ाइलों को सम्‍मिलित करें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल1/का/पथ फ़ाइल2/का/पथ ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फ़ाइल/का/पथ</span>

- आउटपुट फ़ाइल में कई फ़ाइलें जोड़ें:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल1/का/पथ फ़ाइल2/का/पथ ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आउटपुट_फ़ाइल/का/पथ</span>

- फ़ाइल की सामग्री को अनबफर्ड ([u]nbuffered) मोड में आउटपुट फ़ाइल में कॉपी करें:

`cat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty12</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty13</span>

- फ़ाइल में `stdin` लिखें:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- संख्या ([n]umber) सभी आउटपुट लाइनें:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>

- गैर-मुद्रण योग्य और खाली स्थान वाले वर्ण प्रदर्शित करें (`M-` उपसर्ग के साथ यदि गैर-ASCII है):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फ़ाइल/का/पथ</span>