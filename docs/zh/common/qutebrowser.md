---
layout: page
title: common/qutebrowser (中文)
description: "一个基于 PyQt5 的键盘驱动、类似 vim 的浏览器。"
content_hash: 81e07d6cbb98ff3c257103b426dd6e03921b7e21
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/qutebrowser.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qutebrowser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qutebrowser

一个基于 PyQt5 的键盘驱动、类似 vim 的浏览器。
更多信息：<https://qutebrowser.org/>.

- 使用指定存储目录打开 qutebrowser：

`qutebrowser --basedir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 使用临时设置打开 qutebrowser 实例：

`qutebrowser --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content.geolocation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>

- 恢复一个 qutebrowser 实例的指定会话：

`qutebrowser --restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名称</span>

- 启动 qutebrowser，使用指定方式打开所有 URL：

`qutebrowser --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window</span>

- 使用临时基础目录打开 qutebrowser，并以 JSON 格式将日志打印到 `stdout`：

`qutebrowser --temp-basedir --json-logging`
