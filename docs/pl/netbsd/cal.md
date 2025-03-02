---
layout: page
title: netbsd/cal (polski)
description: "Wyświetl kalendarz."
content_hash: 056abb3ef2e4645ff255a82589e904d077009587
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/netbsd/cal.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/netbsd/cal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/netbsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Wyświetl kalendarz.
Więcej informacji: <https://man.netbsd.org/cal.1>.

- Wyświetl kalendarz na bieżący miesiąc:

`cal`

- Wyświetl kalendarz na określony rok:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl kalendarz dla określonego miesiąca i roku:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl cały kalendarz na bieżący rok z użyciem dni [j]uliańskich (dni liczone od 1, począwszy od 1 stycznia):

`cal -y -j`

- Wyróżnij (z ang. [h]ighlight) dzisiejszą datę i wyświetl [3] miesiące ją obejmujące:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl 2 miesiące przed (z ang. [B]efore) i 3 po (z ang. [A]fter) określonym [m]iesiącu bieżącego roku:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>

- Wyświetl określoną liczbę miesięcy przed i po ([C]ontext) określonym miesiącu:

`cal -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiące</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>

- Określ początkowy [d]zień tygodnia (0: niedziela, 1: poniedziałek, ..., 6: sobota):

`cal -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..6</span>
