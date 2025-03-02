---
layout: page
title: linux/kde-builder (English)
description: "Easily build KDE components from its source repositories."
content_hash: 5bdf9bfbaa52a5fc8824527f0ebf979b74b46854
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/linux/kde-builder.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/kde-builder.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kde-builder

Easily build KDE components from its source repositories.
Drop-in replacement for `kdesrc-build`.
More information: <https://kde-builder.kde.org/en/cmdline/cmdline-usage.html>.

- Initialize `kde-builder`:

`kde-builder --generate-config && kde-builder --install-distro-packages`

- Compile a KDE component and its dependencies from the source:

`kde-builder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Compile a component without updating its local code and without compiling its [D]ependencies:

`kde-builder --no-src --no-include-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- [r]efresh the build directories before compiling:

`kde-builder --refresh-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Resume compilation from a specific dependency:

`kde-builder --resume-from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependency_component</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>

- Run a component with a specified executable name:

`kde-builder --run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable_name</span>

- Build all configured components:

`kde-builder`

- Use system libraries in place of a component if it fails to build:

`kde-builder --no-stop-on-failure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">component_name</span>
