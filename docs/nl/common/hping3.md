---
layout: page
title: common/hping3 (Nederlands)
description: "Geavanceerd pinghulpprogramma dat protocollen ondersteunt zoals TCP, UDP en IP."
content_hash: dbe0d6df59e46c915b7513f3137c7bcdfa0f909e
last_modified_at: 2023-11-24
related_topics:
  - title: English version
    url: /en/common/hping3.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hping3.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hping3

Geavanceerd pinghulpprogramma dat protocollen ondersteunt zoals TCP, UDP en IP.
Dit kan het beste uitgevoerd worden met extra priveleges.
Meer informatie: <https://github.com/antirez/hping>.

- Ping een bestemming met 4 ICMP ping aanvragen:

`hping3 --icmp --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_of_hostnaam</span>

- Ping een IP addres over UDP op poort 80:

`hping3 --udp --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_of_hostnaam</span>

- Scan TCP poort 80, maar scan vanaf de specifieke lokale bronpoort 5090:

`hping3 --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --baseport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5090</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_of_hostnaam</span>

- Traceroute met behulp van een TCP scan naar een specifieke bestemmingspoort:

`hping3 --traceroute --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_of_hostnaam</span>

- Scan een set van TCP poorten op een specifiek IP adres:

`hping3 --scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,3000,9000</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_of_hostnaam</span>

- Voer een TCP ACK scan uit om te checken of een gegeven host nog leeft:

`hping3 --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --verbose --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --ack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_of_hostnaam</span>

- Voer een charge test uit op poort 80:

`hping3 --flood --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --syn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_of_hostnaam</span>
