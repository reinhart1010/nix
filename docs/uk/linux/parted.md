---
layout: page
title: linux/parted (українська)
description: "Програма для роботи з розділами."
content_hash: a7c9cd431a7740c9eb9534dae30fce1e1c905e50
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/parted.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/parted.html
    icon: bi bi-globe
tldri18n_status: 2
---
# parted

Програма для роботи з розділами.
Дивіться також: `partprobe`.
Більше інформації: <https://www.gnu.org/software/parted/parted.html>.

- Перелічити розділи на всіх блокових пристроях:

`sudo parted --list`

- Запустити інтерактивний режим із вибраним диском:

`sudo parted `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Створити нову таблицю розділів указаного типу міток:

`sudo parted --script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` mklabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun</span>

- Показати інформацію про розділ в інтерактивному режимі:

`print`

- Вибрати диск в інтерактивному режимі:

`select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Створити розділ на 16 ГБ із зазначеною файловою системою в інтерактивному режимі:

`mkpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary|logical|extended</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16G</span>

- Змінити розмір розділу в інтерактивному режимі:

`resizepart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">кінцева_позиція_розділу</span>

- Видалити розділ в інтерактивному режимі:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
