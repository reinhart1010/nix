---
layout: page
title: linux/gsettings (English)
description: "Query and modify dconf settings with schema validation."
content_hash: aad65580e61d73d2ea48fc83624bd71219efdf8c
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/gsettings.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gsettings

Query and modify dconf settings with schema validation.
More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>.

- Set the value of a key. Fails if the key doesn't exist or the value is out of range:

`gsettings set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example-key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Print the value of a key or the schema-provided default if the key has not been set in `dconf`:

`gsettings get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example-key</span>

- Unset a key, so that its schema default value will be used:

`gsettings reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example-key</span>

- Display all (non-relocatable) schemas, keys, and values:

`gsettings list-recursively`

- Display all keys and values (default if not set) from one schema:

`gsettings list-recursively `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>

- Display schema-allowed values for a key (helpful with enum keys):

`gsettings range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example-key</span>

- Display the human-readable description of a key:

`gsettings describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.example.schema</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example-key</span>
