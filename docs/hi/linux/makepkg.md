---
layout: page
title: linux/makepkg (हिन्दी)
description: "एक पैकेज बनाएं जिसका उपयोग `pacman` के साथ किया जा सकता है।"
content_hash: a0dee540c3d7f011c611f2006010ceb759e2188f
last_modified_at: 2023-10-19
related_topics:
  - title: English version
    url: /en/linux/makepkg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/makepkg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># makepkg

एक पैकेज बनाएं जिसका उपयोग `pacman` के साथ किया जा सकता है।
डिफ़ॉल्ट रूप में वर्तमान काम कर रहे डायरेक्टरी में `PKGBUILD` फ़ाइल का उपयोग करता है।
अधिक जानकारी: <https://man.archlinux.org/man/makepkg.8>.

- एक पैकेज बनाएं:

`makepkg`

- एक पैकेज बनाएं और इसके डिपेंडेंसियों को इंस्टॉल करें:

`makepkg --syncdeps`

- एक पैकेज बनाएं, इसके डिपेंडेंसियों को इंस्टॉल करें, और फिर इसे सिस्टम में इंस्टॉल करें:

`makepkg --syncdeps --install`

- एक पैकेज बनाएं, लेकिन स्रोत के हैश की जाँच को छोड़ें:

`makepkg --skipchecksums`

- सफलता पूर्वक बनाने के बाद काम के डायरेक्टरी को साफ करें:

`makepkg --clean`

- स्रोतों के हैश की जाँच करें:

`makepkg --verifysource`

- स्रोत जानकारी बनाएं और `.SRCINFO` में सहेजें:

`makepkg --printsrcinfo > .SRCINFO`