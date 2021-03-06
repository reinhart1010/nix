---
layout: page
title: common/at (中文)
description: "在一段时间后，执行单次命令。"
content_hash: d5ae468c864cdeb7a578d0939837a6ab86147cd5
related_topics:
  - title: English version
    url: /en/common/at.html
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
---
# at

在一段时间后，执行单次命令。
atd 服务（或 atrun）需要处于运行状态，以保证命令成功执行。
更多信息：<https://manned.org/at>.

- 5 分钟后，执行标准输入中的命令（命令输入完成后按 `Ctrl + D`）：

`at now + `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 minutes</span>

- 在今天上午 10:00 执行标准输入中的命令：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>

- 下周二晚上 9:30 执行指定文件中包含的命令：

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9:30 PM Tue</span>
