# Changelog

Rendered by CI and committed back at the end of a release -- do not edit by
hand. Release notes also appear on the GitHub Releases page, one per tag.

## [1.0.4](https://github.com/hyperi-io/ci-test-python-lib/compare/v1.0.3...v1.0.4) (2026-09-17)

### Bug Fixes

* bump dulwich, urllib3 past advisories ([e95ff0e](https://github.com/hyperi-io/ci-test-python-lib/commit/e95ff0ea69edd0d016eab78e6ab061937eb01864))
* **ci:** stop this fixture reaching a public registry, adopt org Renovate ([#5](https://github.com/hyperi-io/ci-test-python-lib/issues/5)) ([b5d805f](https://github.com/hyperi-io/ci-test-python-lib/commit/b5d805f9d06b5414b13558851e661891d1dd29f7)), closes [hyperi-io/hyperi-ci#79](https://github.com/hyperi-io/hyperi-ci/issues/79)
* drop deprecated .releaserc.yaml (central semantic-release default) ([48fead4](https://github.com/hyperi-io/ci-test-python-lib/commit/48fead450a73c5ffdd631c32ee402540d54c0927))
* **meta:** drop the em-dash from the project description ([037715a](https://github.com/hyperi-io/ci-test-python-lib/commit/037715a7d79c918ff4ce213a014b239ab2c56d01))
* **meta:** use the fleet-wide description format ([67a1449](https://github.com/hyperi-io/ci-test-python-lib/commit/67a1449695576cdb6bed3c9fc1c720f75424aa4c))
* **release:** attach catalogue.yaml to the release ([f348bd5](https://github.com/hyperi-io/ci-test-python-lib/commit/f348bd5526ce1a352c1e588e239f81b4c1675a32)), closes [hyperi-ci#125](https://github.com/hyperi-io/hyperi-ci/issues/125)

## [1.0.3](https://github.com/hyperi-io/ci-test-python-lib/compare/v1.0.2...v1.0.3) (2026-04-30)


### Bug Fixes

* add dev dep group with ruff/ty/pytest so CI can spawn ruff ([45ba87d](https://github.com/hyperi-io/ci-test-python-lib/commit/45ba87d41b234263943a9ec2ca2169165a211f0e))
* add pytest-cov to dev deps so coverage flags work ([1bd6f25](https://github.com/hyperi-io/ci-test-python-lib/commit/1bd6f25b03c82f64b2c43bdde6053e06d94b1a31))
* declare hyperi-pylib[metrics] for psutil at import time ([47576c6](https://github.com/hyperi-io/ci-test-python-lib/commit/47576c6a94fe79b5a3a7f44370929b93019d23f9))
* greenfield as ci-test-python-lib — hyperi-pylib re-export ([b839037](https://github.com/hyperi-io/ci-test-python-lib/commit/b83903760b8ce4683b9172069fd5db192d604e18))
* refresh init output and target=oss ([b378c8d](https://github.com/hyperi-io/ci-test-python-lib/commit/b378c8d5df812902b459e0d53c7a32e759a53cd8))

## [1.0.2](https://github.com/hyperi-io/ci-test-python-package/compare/v1.0.1...v1.0.2) (2026-03-02)


### Bug Fixes

* add build.type to config ([d3d4172](https://github.com/hyperi-io/ci-test-python-package/commit/d3d4172ca6ff6c35af2541bf2f3ebc010d2eb65c))

## [1.0.1](https://github.com/hyperi-io/ci-test-python-package/compare/v1.0.0...v1.0.1) (2026-03-02)


### Bug Fixes

* remove container requirement for default GH runner ([614febe](https://github.com/hyperi-io/ci-test-python-package/commit/614febe6c90f9f80b96d57271813cecb2e8878de))

# 1.0.0 (2026-03-02)


### Features

* initial scaffold for CI test project ([1e33e62](https://github.com/hyperi-io/ci-test-python-package/commit/1e33e62380112ed235bc494c25b161e65c115ee6))
