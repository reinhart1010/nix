---
layout: page
title: common/docker (中文 (繁體, 台灣))
description: "管理 Docker 容器和映像檔。"
content_hash: b1f64e4458ffb3b95d8744cbcc3a6042bf212a40
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/common/docker.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker

管理 Docker 容器和映像檔。
此命令也有關於其子命令的文件，例如：`docker run`.
更多資訊：<https://docs.docker.com/engine/reference/commandline/cli/>.

- 列出目前正在運行的 docker 容器：

`docker ps`

- 列出所有 docker 容器（包括停止的容器）：

`docker ps -a`

- 透過映像檔啟動容器，並為容器命名：

`docker run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名稱</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">映像檔</span>

- 啟動或停止現有容器：

`docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名稱</span>

- 從 docker registry 中拉取映像檔：

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">映像檔</span>

- 從正在運行的容器內打開一個 shell：

`docker exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名稱</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- 刪除一個停止的容器：

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名稱</span>

- 獲取並查看容器的日誌：

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">容器名稱</span>
