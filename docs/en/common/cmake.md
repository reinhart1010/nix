---
layout: page
title: common/cmake (English)
description: "Cross-platform build automation system, that generates recipes for native build systems."
content_hash: a0e9bfda20ab1adb2c123cd4d7bb76efc2c5f7f7
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cmake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cmake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmake.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cmake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmake

Cross-platform build automation system, that generates recipes for native build systems.
More information: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Generate a build recipe in the current directory with `CMakeLists.txt` from a project directory:

`cmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_directory</span>

- Generate a build recipe, with build type set to `Release` with CMake variable:

`cmake `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_directory</span>` -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CMAKE_BUILD_TYPE=Release</span>

- Generate a build recipe using `generator_name` as the underlying build system:

`cmake -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generator_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_directory</span>

- Use a generated recipe in a given directory to build artifacts:

`cmake --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>

- Install the build artifacts into `/usr/local/` and strip debugging symbols:

`cmake --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>` --strip`

- Install the build artifacts using the custom prefix for paths:

`cmake --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>` --strip --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run a custom build target:

`cmake --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/build_directory</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>

- Display help, obtain a list of generators:

`cmake --help`
