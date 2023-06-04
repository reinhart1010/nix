---
layout: page
title: common/jps (English)
description: "Show JVM process status of current user."
content_hash: f8abcdf4b3e3e31f5c4b2c9843cd7e867c23799c
last_modified_at: 2023-06-04
related_topics:
  - title: 中文 version
    url: /zh/common/jps.html
    icon: bi bi-globe
---
# jps

Show JVM process status of current user.
More information: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jps.html>.

- List all JVM processes:

`jps`

- List all JVM processes with only PID:

`jps -q`

- Display the arguments passed to the processes:

`jps -m`

- Display the full package name of all processes:

`jps -l`

- Display the arguments passed to the JVM:

`jps -v`
