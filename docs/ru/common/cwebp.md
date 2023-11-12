---
layout: page
title: common/cwebp (русский)
description: "Сжимает файл изображения в формат WebP."
content_hash: a464571396b6f0d199b3608fd5a08f5b78d42a3b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cwebp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cwebp

Сжимает файл изображения в формат WebP.
Больше информации: <https://developers.google.com/speed/webp/docs/cwebp>.

- Сжать WebP со стандартными настройками (q = 75) с сохранением в выходной файл:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/изображению</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/результату.webp</span>

- Сжать WebP с наилучшим качеством и наибольшим размером файла:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/изображению</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/результату.webp</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Сжать WebP с наихудшим качеством и наименьшим размером файла:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/изображению</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/результату.webp</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>

- Сжать WebP с изменением размера изображения:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/изображению</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/результату.webp</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>

- Сжать WebP с удалением информации о прозрачности:

`cwebp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/изображению</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/результату.webp</span>` -noalpha`
