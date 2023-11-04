---
layout: page
title: linux/checkupdates (हिन्दी)
description: "आर्क लिनक्स में लंबित अद्यतनों की जाँच करने के लिए उपकरण।"
content_hash: dd336b246be11ca121347ec4a1cda64deaf54c88
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/linux/checkupdates.html
    icon: bi bi-globe
---
# checkupdates

आर्क लिनक्स में लंबित अद्यतनों की जाँच करने के लिए उपकरण।
अधिक जानकारी: <https://man.archlinux.org/man/checkupdates.8>.

- लंबित अद्यतनों की सूची बनाएं:

`checkupdates`

- लंबित अद्यतनों की सूची बनाएं और पैकेजों को पैक्मैन कैश में डाउनलोड करें:

`checkupdates --download`

- विशिष्ट पैक्मैन डेटाबेस का उपयोग करके लंबित अद्यतनों की सूची बनाएं:

`CHECKUPDATES_DB=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">निर्देशिका/का/पथ</span>` checkupdates`

- सहायता प्रदर्शित करें:

`checkupdates --help`
