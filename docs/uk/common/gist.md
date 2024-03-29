---
layout: page
title: common/gist (українська)
description: "Завантажує код у https://gist.github.com."
content_hash: 3cac6a551839a44ecb2e7aa45961510b9fb0f934
last_modified_at: 2023-12-27
related_topics:
  - title: English version
    url: /en/common/gist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gist

Завантажує код у https://gist.github.com.
Більше інформації: <https://github.com/defunkt/gist>.

- Увійти в gist на цьому комп'ютері:

`gist --login`

- Створити gist з будь-якої кількості текстових файлів:

`gist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_файлу.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_файлу2.txt</span>

- Створити приватний gist з описом:

`gist --private --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Змістовний опис</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_файлу.txt</span>

- Прочитати контент з `stdin` і створити gist з цього:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "привіт світ"</span>` | gist`

- Перелічити свої публічні та приватні gist:

`gist --list`

- Перелічити всі публічні gist будь-якого користувача:

`gist --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_користувача</span>

- Оновити gist за допомогою ID з URL:

`gist --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GIST_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_файлу.txt</span>
