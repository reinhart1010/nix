---
layout: page
title: common/cb (فارسی)
description: "بریدن، رونوشت و چسباندن هرچیزی در ترمینال."
content_hash: 76e1851339d8c538c6e2040c07e353f7d877af49
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/common/cb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cb

بریدن، رونوشت و چسباندن هرچیزی در ترمینال.
اطلاعات بیشتر: <https://github.com/Slackadays/Clipboard>.

- نمایش تمام کلیپ بوردها:

`cb`

- رونوشت یک فایل به کلیپ بورد:

`cb copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- کپی متن دلخواه به کلیپ بورد:

`cb copy "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Some example text</span>`"`

- رونوشت داده ی هدایت شده به داخل در کلیپ بورد:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Some example text</span>`" | cb`

- چسباندن محتوای کلیپ بورد:

`cb paste`

- هدایت محتوای کلیپ بورد به خارج:

`cb | cat`

- نمایش تاریخچه کلیپ بورد:

`cb history`

- نمایش اطلاعات کلیپ بورد:

`cb info`
