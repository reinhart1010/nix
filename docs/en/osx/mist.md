---
layout: page
title: osx/mist (English)
description: "MIST - macOS Installer Super Tool."
content_hash: 53c710c524c989f1076770c7d82e4743065ccdbb
last_modified_at: 2024-06-26
tldri18n_status: 2
---
# mist

MIST - macOS Installer Super Tool.
Automatically download macOS Firmwares/Installers.
More information: <https://github.com/ninxsoft/mist-cli>.

- List all available macOS Firmwares for Apple Silicon Macs:

`mist list firmware`

- List all available macOS Installers for Intel Macs, including Universal Installers for macOS Big Sur and later:

`mist list installer`

- List all macOS Installers that are compatible with this Mac, including Universal Installers for macOS Big Sur and later:

`mist list installer --compatible`

- List all available macOS Installers for Intel Macs, including betas, also including Universal Installers for macOS Big Sur and later:

`mist list installer --include-betas`

- List only the latest macOS Sonoma Installer for Intel Macs, including Universal Installers for macOS Big Sur and later:

`mist list installer --latest "macOS Sonoma"`

- List and export macOS Installers to a CSV file:

`mist list installer --export "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/export.csv</span>`"`

- Download the latest macOS Sonoma Firmware for Apple Silicon Macs, with a custom name:

`mist download firmware "macOS Sonoma" --firmware-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Install %NAME% %VERSION%-%BUILD%.ipsw</span>`"`

- Download a specific macOS Installer version for Intel Macs, including Universal Installers for macOS Big Sur and later:

`mist download installer "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">13.5.2</span>`" application`
