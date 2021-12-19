---
layout: page
title: common/weasyprint (русский)
description: "Переводить HTML в PDF или PNG."
content_hash: 85588acd865a2fbb33ec39f8a1c36e1e2ed10803
related_topics:
  - title: English version
    url: /en/common/weasyprint.html
    icon: bi bi-globe
---
# weasyprint

Переводить HTML в PDF или PNG.
Больше информации: <https://weasyprint.org/>.

- Перевести HTML файл в PDF:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/входного.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/выходного.pdf</span>

- Перевести HTML файл в PNG, включая дополнительные пользовательские таблицы стилей:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/входного.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/выходного.png</span>` --stylesheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/таблицы-стилей.css</span>

- При переводе выводить дополнительную отладочную информацию:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/входного.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/выходного.pdf</span>` --verbose`

- При выводе в PNG указать нестандартное разрешение:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/входного.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/выходного.png</span>` --resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- Во входном HTML файле указать базовый URL для относительных URLs:

`weasyprint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/входного.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/выходного.png</span>` --base-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_или_имя-файла</span>
