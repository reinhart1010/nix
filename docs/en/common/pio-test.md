---
layout: page
title: common/pio-test (English)
description: "Run local tests on a PlatformIO project."
content_hash: 11fe1db01a6e992824e62bb14e940216edb77d7f
---
# pio test

Run local tests on a PlatformIO project.
More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- Run all tests in all environments of the current PlatformIO project:

`pio test`

- Test only specific environments:

`pio test --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment1</span>` --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">environment2</span>

- Run only tests whose name matches a specific glob pattern:

`pio test --filter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`

- Ignore tests whose name matches a specific glob pattern:

`pio test --ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`

- Specify a port for firmware uploading:

`pio test --upload-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upload_port</span>

- Specify a custom configuration file for running the tests:

`pio test --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/platformio.ini</span>
