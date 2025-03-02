---
layout: page
title: common/xkill (中文)
description: "在图形会话中以交互方式终止窗口。"
content_hash: 5c279af67622060d01e2b33962e5a2b49ff1c58d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/xkill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/xkill.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/xkill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/xkill.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/xkill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xkill.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/xkill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xkill

在图形会话中以交互方式终止窗口。
另请参阅：`kill`、`killall`。
更多信息：<https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- 按下鼠标左键时终止鼠标选择的窗口（按下任何其他鼠标按钮可取消）：

`xkill`

- 按下任意鼠标按键时终止鼠标选择的窗口：

`xkill -button any`

- 终止具有特定 ID 的窗口（使用 `xwininfo` 获取有关窗口的信息）：

`xkill -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
