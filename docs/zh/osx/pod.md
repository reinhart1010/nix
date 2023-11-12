---
layout: page
title: osx/pod (中文)
description: "Swift 和 Objective-C Cocoa 项目的依赖关系管理。"
content_hash: 6d92f4be0c142f97aac158c42dde411584e9a39b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/pod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pod

Swift 和 Objective-C Cocoa 项目的依赖关系管理。
更多信息：<https://guides.cocoapods.org/terminal/commands.html>.

- 为当前项目初始化包含默认内容的 podfile：

`pod init`

- 下载并安装 pod 文件中定义的所有 pod（以前未安装）：

`pod install`

- 列出所有可用的 pod：

`pod list`

- 显示过时的 pod（当前安装的 pod）：

`pod outdated`

- 将当前安装的所有 pod 更新到其最新版本：

`pod update`

- 将特定（以前安装的）pod 更新为其最新版本：

`pod update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_名</span>

- 从 Xcode 项目中删除 CocoaPods：

`pod deintegrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcode_项目</span>
