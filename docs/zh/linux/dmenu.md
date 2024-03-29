---
layout: page
title: linux/dmenu (中文)
description: "动态菜单。"
content_hash: f8864dde9487db21e9ba4efbf0d984ebbc62f63b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/dmenu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmenu

动态菜单。
根据文本输入创建菜单，其中每一项都在新行中。
更多信息：<https://manned.org/dmenu>.

- 显示 `ls` 命令输出的菜单：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>` | dmenu`

- 显示包含自定义项目的菜单，并用新行（`\n`）分隔：

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | dmenu`

- 让用户在多个项目之间进行选择，然后将所选项目保存到文件中：

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>`" | dmenu > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color.txt</span>

- 在特定的监视器上启动 `dmenu`：

`ls | dmenu -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 在屏幕底部显示 `dmenu`：

`ls | dmenu -b`
