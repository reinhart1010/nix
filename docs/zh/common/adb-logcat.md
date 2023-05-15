---
layout: page
title: common/adb-logcat (中文)
description: "转储系统消息日志。"
content_hash: 518682c8ca0272949e85967963830790d58cde77
last_modified_at: 2023-05-15
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-logcat.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adb-logcat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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

- 显示特定 PID 的日志：

`adb logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 显示某个特定软件包的进程日志：

`adb logcat --pid=$(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>`)`

- 给日志着色（通常与过滤器一起使用）:

`adb logcat -v color`
