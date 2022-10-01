---
layout: page
title: common/adb-logcat (中文)
description: "转储系统消息日志。"
content_hash: e399235fe21326ec22ad1ce030cf994f1702d6da
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb-logcat

转储系统消息日志。
更多信息：<https://developer.android.com/studio/command-line/logcat>.

- 显示系统日志：

`adb logcat`

- 显示符合正则表达式的行：

`adb logcat -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式</span>

- 显示特定优先级下（V：详细，D：调试，I：信息，W：警告，E：错误，F：严重错误，S：静默）标记的日志，过滤掉其他标记：

`adb logcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标记</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">最低优先级</span>` *:S`

- 在详细（V）模式下显示 React Native 应用程序的日志，静默（S）其他标记：

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- 显示优先级为警告（W）及以上的所有标签的日志：

`adb logcat *:W`

- 给日志着色（通常与过滤器一起使用）:

`adb logcat -v color`
