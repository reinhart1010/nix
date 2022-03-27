---
layout: page
title: windows/scoop-bucket (中文)
description: "管理 bucket: 包含描述 scoop 应如何安装应用程序的文件的 Git 存储库。"
content_hash: 30930b79eaa89a724c6b3afe5749290ca4822629
related_topics:
  - title: Deutsch version
    url: /de/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop-bucket.html
    icon: bi bi-globe
---
# scoop bucket

管理 bucket: 包含描述 scoop 应如何安装应用程序的文件的 Git 存储库。
如果 Scoop 不知道 bucket 在哪里，则必须指定其存储库位置。
更多信息：<https://github.com/lukesampson/scoop/wiki/Buckets>.

- 列出所有正在使用的 bucket：

`scoop bucket list`

- 列出所有已知 bucket：

`scoop bucket known`

- 按名称添加一个已知 bucket：

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 通过名称和 Git 存储库 URL 添加未知 bucket：

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/repository.git</span>

- 按名称删除 bucket：

`scoop bucket rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
