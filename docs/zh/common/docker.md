---
layout: page
title: common/docker (中文)
description: "管理 Docker 容器和镜像。"
content_hash: bc3dc03a5e8695d3d275b143303fde20a602bb22
last_modified_at: 2024-01-02
related_topics:
  - title: Deutsch version
    url: /de/common/docker.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/docker.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/docker.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker

管理 Docker 容器和镜像。
此命令也有关于其子命令的文件，例如：`docker run`.
更多信息：<https://docs.docker.com/engine/reference/commandline/cli/>.

- 列出所有 docker 容器（包括停止的容器）：

`docker ps --all`

- 透过镜像启动容器，并为容器命名：

`docker run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像</span>

- 启动或停止现有容器：

`docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名称</span>

- 从 docker registry 中拉取镜像：

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">镜像</span>

- 从正在运行的容器内打开一个 shell：

`docker exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- 删除一个停止的容器：

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名称</span>

- 获取并查看容器的日志：

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名称</span>
