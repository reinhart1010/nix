---
layout: page
title: linux/tmt (中文)
description: "创建、运行和调试测试的测试管理工具。"
content_hash: 8a51a4778e07303d6d094afb87bf0d65fb28a2e8
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/linux/tmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmt

创建、运行和调试测试的测试管理工具。
诸如`运行`、`尝试`等子命令，均有相应的用法文档。
更多信息：<https://tmt.readthedocs.io>.

- 列举可用的测试、计划和用户故事：

`tmt`

- 初始化测试管理工具的文件/项目结构：

`tmt init`

- 基于模板和链接创建新的测试：

`tmt test create --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">beakerlib</span>` --link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">verifies:issue#1234</span>

- 列出可用的测试、计划和用户故事：

`tmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test|plan|story</span>` ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- 在给定的上下文中显示详细的测试元数据：

`tmt --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch=aarch64</span>` test show`

- 根据说明书验证测试管理工具文件的有效性：

`tmt lint`

- 使用筛选条件：

`tmt tests ls --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag:foo</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tier:0</span>

- 显示帮助：

`tmt --help`
