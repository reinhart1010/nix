---
layout: page
title: common/dog (українська)
description: "Утиліта пошуку DNS."
content_hash: e7c9a567c0c3cd689da9e2ff3dbe158807ff8018
related_topics:
  - title: English version
    url: /en/common/dog.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dog

Утиліта пошуку DNS.
Вона має кольоровий вихід, підтримує протоколи DNS-over-TLS і DNS-over-HTTPS та може видавати JSON.
Більше інформації: <https://dns.lookup.dog>.

- Шукає IP-адреси пов'язані з іменем хоста (A records):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Запитує тип записів MX, пов’язаних із заданим доменним ім’ям:

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX`

- Вкажіть конкретний DNS-сервер для запиту (наприклад, Cloudflare):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- Запит через TCP, а не UDP:

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` --tcp`

- Запитує тип записів MX, пов’язаних із заданим доменним ім’ям через TCP, використовуючи явні аргументи:

`dog --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --type MX --nameserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` --tcp`

- Шукає IP-адреси, пов’язані з іменем хоста (записи A), за допомогою DNS через HTTPS (DoH):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --https @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://cloudflare-dns.com/dns-query</span>
