---
layout: page
title: common/ansiweather (中文)
description: "一个 shell 脚本，用于在终端中显示当前的天气状况。"
content_hash: d157d36041c6d032c07c5e51a9f6e97a8b04910d
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/ansiweather.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansiweather.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansiweather

一个 shell 脚本，用于在终端中显示当前的天气状况。
更多信息：<https://github.com/fcambus/ansiweather>.

- 使用公制单位显示 Rzeszow, Poland 接下来 5 天的天气预报：

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- 显示带符号和日光数据信息的天气预报：

`ansiweather -F -s true -d true`

- 显示带风力等级和湿度信息的天气预报：

`ansiweather -w true -h true`
