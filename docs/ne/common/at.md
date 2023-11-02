---
layout: page
title: common/at (नेपाली)
description: "पछि एक पटक आदेशहरू कार्यान्वयन गर्छ।"
content_hash: e346fbb2ead6035bcae66f7d776a40b00258d63a
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
---
# at

पछि एक पटक आदेशहरू कार्यान्वयन गर्छ।
वास्तविक कार्यान्वयनको लागि service atd(अथवा atrun) चलिरहेको हुनुपर्छ।
थप जानकारी: <https://manned.org/at>।

- मानक इनपुट बाट आदेशहरू ५ मिनटमा कार्यान्वयन गर्नुहोस् (सकिएपछि `Ctrl +D` थिच्नुहोस्):

`at now + 5 minutes`

- मानक इनपुट बाट आदेश आज के बिहान को १० बजे कार्यान्वयन गर्नुहोस्:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at 1000`

- एउटा दिइएको फाइलबाट अर्को मङ्गलबार आदेशहरु कार्यान्वयन गर्नुहोस्:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">फाइल/को/पथ</span>` 9:30 PM Tue`
