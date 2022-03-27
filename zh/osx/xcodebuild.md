---
layout: page
title: osx/xcodebuild (中文)
description: "构建 Xcode 项目。"
content_hash: ed132dfa55678cdc2af3a6a5bc7fe41159dac9d6
related_topics:
  - title: English version
    url: /en/osx/xcodebuild.html
    icon: bi bi-globe
---
# xcodebuild

构建 Xcode 项目。

- 构建工作区：

`xcodebuild -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">工作区名.工作区</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主题名</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置名</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYMROOT_路径</span>

- 构建项目：

`xcodebuild -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标名</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置名</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYMROOT_路径</span>

- 显示 SDK：

`xcodebuild -showsdks`
