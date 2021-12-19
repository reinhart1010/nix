---
layout: page
title: common/composer (English)
description: "A package-based dependency manager for PHP projects."
content_hash: d665334c814fe7a844cd5468d92134a9cced051e
related_topics:
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

- Add a package as a dependency for this project, adding it to `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package_name</span>

- Install all the dependencies in this project's `composer.json` and create `composer.lock`:

`composer install`

- Uninstall a package from this project, removing it as a dependency from `composer.json`:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package_name</span>

- Update all the dependencies in this project's `composer.json` and note versions in `composer.lock` file:

`composer update`

- Update composer lock only after updating `composer.json` manually:

`composer update --lock`

- Learn more about why a dependency can't be installed:

`composer why-not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/package_name</span>

- Update composer to its latest version:

`composer self-update`
