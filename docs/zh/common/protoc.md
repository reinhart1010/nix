---
layout: page
title: common/protoc (中文)
description: "解析 Google Protobuf `.proto` 文件并生成指定语言的输出。"
content_hash: 277532bb2524ca11984030f888418ba906844b06
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/protoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protoc

解析 Google Protobuf `.proto` 文件并生成指定语言的输出。
更多信息：<https://developers.google.com/protocol-buffers>.

- 从 `.proto` 文件生成 Python 代码：

`protoc --python_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输入文件.proto</span>

- 从一个导入其他 `.proto` 文件的 `.proto` 文件生成 Java 代码:

`protoc --java_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出目录</span>` --proto_path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/导入搜索路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输入文件.proto</span>

- 生成多种语言的代码：

`protoc --csharp_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/c#_输出目录</span>` --js_out=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/js_输出目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输入文件.proto</span>
