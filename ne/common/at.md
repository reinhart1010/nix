---
layout: page
title: common/at (नेपाली)
description: "पछि एक पटक आदेशहरू कार्यान्वयन गर्छ।"
content_hash: 3b835819605eb3a55b96f675960bb8904e352693
related_topics:
  - title: English version
    url: /en/common/at.html
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
वास्तविक कार्यान्वयनको लागि service atd(अथवा atrun) चलिरहेको हुनुपर्छ ।
थप जानकारी: <https://man.archlinux.org/man/at.1>.

- standard input बाट आदेशहरू ५ मिनटमा कार्यान्वयन गर्नुहोस् (सकिएपछि `Ctrl +D` थिच्नुहोस्):

`at now + 5 minutes`

- standard input बाट आदेश आजको बिहानको १० बजे कार्यान्वयन गर्नुहोस्:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at 1000`

- एउटा दिइएको फाइलबाट अर्को मङ्गलबार आदेशहरु कार्यान्वयन गर्नुहोस्:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` 9:30 PM Tue`
