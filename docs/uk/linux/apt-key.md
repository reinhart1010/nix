---
layout: page
title: linux/apt-key (українська)
description: "Утиліта керування ключами для диспетчера пакетів APT в Debian та Ubuntu."
content_hash: 638cd9f6e71173a54867b8f881e49907c8e0798a
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-key.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-key.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-key.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-key.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-key.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-key

Утиліта керування ключами для диспетчера пакетів APT в Debian та Ubuntu.
Примітка: `apt-key` застарілий (за винятком використання `apt-key del` у сценаріях підтримки).
Більше інформації: <https://manned.org/apt-key.8>.

- Список довірених ключів:

`apt-key list`

- Додати ключ до довіреного сховища ключів:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public_key_file.asc</span>

- Видалити ключ з довіреного сховища ключів:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>

- Додайте віддалений ключ до надійного сховища ключів:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/filename.key</span>` | apt-key add -`

- Додати ключ із сервера ключів лише з ідентифікатором ключа:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KEYID</span>
