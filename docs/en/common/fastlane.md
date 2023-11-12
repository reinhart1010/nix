---
layout: page
title: common/fastlane (English)
description: "Build and release mobile applications."
content_hash: 4c7ef9ac8bc7ce85044b68d969240b9b655fc6c2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# fastlane

Build and release mobile applications.
More information: <https://docs.fastlane.tools/actions/>.

- Build and sign the iOS application in the current directory:

`fastlane run build_app`

- Run `pod install` for the project in the current directory:

`fastlane run cocoapods`

- Delete the derived data from Xcode:

`fastlane run clear_derived_data`

- Remove the cache for pods:

`fastlane run clean_cocoapods_cache`
