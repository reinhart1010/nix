---
layout: page
title: common/composer (English)
description: "A package-based dependency manager for PHP projects."
content_hash: 1792c08a588525b86ebf3f2ed2f182e2104cb1ee
last_modified_at: 2023-10-13
related_topics:
  - title: Indonesia version
    url: /id/common/composer.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/composer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/composer.html
    icon: bi bi-globe
---
# composer

A package-based dependency manager for PHP projects.
More information: <https://getcomposer.org/>.

- Interactively create a `composer.json` file:

`composer init`

- Add a package as a dependency for this project, adding an entry to `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package</span>

- Install all the dependencies in this project's `composer.json` and create `composer.lock`:

`composer install`

- Uninstall a package from this project, removing it as a dependency from `composer.json` and `composer.lock`:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package</span>

- Update all the dependencies in this project's `composer.json` and note new versions in `composer.lock` file:

`composer update`

- Update only `composer.lock` after updating `composer.json` manually:

`composer update --lock`

- Learn more about why a dependency can't be installed:

`composer why-not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package</span>

- Update composer to its latest version:

`composer self-update`
