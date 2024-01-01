---
layout: page
title: common/at (中文)
description: "在一段时间后，执行单次命令。"
content_hash: 194d2853f3ec95e46be5645558eb0251817dac5c
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

在一段时间后，执行单次命令。
atd 服务（或 atrun）需要处于运行状态，以保证命令成功执行。
更多信息：<https://manned.org/at>.

- 5 分钟后，执行标准输入中的命令（命令输入完成后按 `Ctrl + D`）：

`at now + 5 minutes`

- 在今天上午 10:00 执行标准输入中的命令：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at 1000`

- 下周二晚上 9:30 执行指定文件中包含的命令：

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` 9:30 PM Tue`
