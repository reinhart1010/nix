---
layout: page
title: common/aapt (中文)
description: "安卓资源包工具（Android Asset Packaging Tools）。"
content_hash: ea13b485c3a2c54242c40096f33ad8595706b52f
related_topics:
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
---
# aapt

安卓资源包工具（Android Asset Packaging Tools）。
该工具可以查看，创建，更新资源压缩包（zip, jar, apk）。
更多信息：<https://elinux.org/Android_aapt>.

- 列出资源压缩包里的内容：

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 查看 APK 包内指定的内容（版本，权限许可等）：

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 打包生成资源压缩包：

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>
