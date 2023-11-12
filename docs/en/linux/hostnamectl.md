---
layout: page
title: linux/hostnamectl (English)
description: "Get or set the hostname of the computer."
content_hash: 77425924701e26e93cdc2d47145d6b14c083b164
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/hostnamectl.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/hostnamectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hostnamectl

Get or set the hostname of the computer.
More information: <https://manned.org/hostnamectl>.

- Get the hostname of the computer:

`hostnamectl`

- Set the hostname of the computer:

`sudo hostnamectl set-hostname "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`"`

- Set a pretty hostname for the computer:

`sudo hostnamectl set-hostname --static "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname.example.com</span>`" && sudo hostnamectl set-hostname --pretty "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`"`

- Reset hostname to its default value:

`sudo hostnamectl set-hostname --pretty ""`
