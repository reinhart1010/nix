---
layout: page
title: linux/at (中文)
description: "在指定时间执行命令。"
content_hash: 54d0fb10b25fc5bbaffbf055bcd42eeb231367d8
related_topics:
  - title: English version
    url: /en/linux/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/at.html
    icon: bi bi-globe
---
# at

在指定时间执行命令。
更多信息：<https://man.archlinux.org/man/at.1>.

- 打开 `at` 提示符创建一组新的定时命令，按 `Ctrl + D` 保存并退出：

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- 运行命令并通过本地电子邮件程序（例如 sendmail）发送运行结果：

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -m`

- 在指定时间执行一个脚本：

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 在二月十八号下午十一点发送系统通知：

`echo "notify-send '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Wake up!</span>`'" | at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11pm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Feb 18</span>
