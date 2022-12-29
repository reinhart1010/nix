---
layout: page
title: common/git-rebase (中文)
description: "将 commits 从一个分支合并到另一个分支上。"
content_hash: 358415f13afc06da9ce30778defd84f809d4ea91
last_modified_at: 2022-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
---
# git rebase

将 commits 从一个分支合并到另一个分支上。
常用于跨分支的 commits 合并，在被合并分支的最头部构建新的 `commit`，表示合并完成。
更多信息：<https://git-scm.com/docs/git-rebase>.

- 在另一个分支的头节点合并当前分支：

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标分支</span>

- 启动交互式的合并任务，允许对提交的内容进行重新排序、省略、合并或修改：

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标分支或 commit 的 hash</span>

- 处理完冲突文件后，继续执行合并任务：

`git rebase --continue`

- 跳过冲突文件，继续执行合并任务：

`git rebase --skip`

- 终止正在执行中的合并任务（例如：对于正处于解决冲突中的任务，将其打断，恢复到合并前的状态）：

`git rebase --abort`

- 将分支的部分 commits 生成新的 `commit`，移动到新分支的头节点：

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标分支</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">当前分支</span>

- 启动交互式的合并任务，对最近提交的 5 个 commits 进行重新排序、省略、合并或修改：

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- 以当前分支优先的策略，自动处理分支间的冲突，执行合并：

`git rebase -X theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支名称</span>
