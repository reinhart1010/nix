---
layout: page
title: osx/shutdown (中文)
description: "关闭并重新启动系统。"
content_hash: b4059e2c0c85f2318521caff7cd8804ae58bc7ec
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

关闭并重新启动系统。
更多信息：<https://keith.github.io/xcode-man-pages/shutdown.8.html>.

- 立即关机：

`shutdown -h now`

- 立即休眠：

`shutdown -s now`

- 立即重启：

`shutdown -r now`

- 倒计时 5 分钟重启：

`shutdown -r "+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`"`

- 在下午 1:00（使用 24 小时时钟）关机：

`shutdown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1300</span>

- 在 2042 年 5 月 10 日上午 11:30 重新启动（输入格式：年年月月日日时时分分）：

`shutdown -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4205101130</span>
