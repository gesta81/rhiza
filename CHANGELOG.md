# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.1] - 2026-01-01

### Added
- GitLab CI/CD workflows with feature parity to GitHub Actions
- CodeQL security workflow
- CodeFactor badge to README
- python-dotenv dependency for tests

### Changed
- Reduced action complexity
- Fixed broken deptry test
- Fixed duplicate workflow runs on PR branches
- Several README.md files updated for GitHub
- Coverage number improvements
- Revisited GitLab workflows
- Dealing with env files

### Fixed
- Marimo notebooks not erroring at build stage in the event of failure
- All Bandit S607 security warnings by using absolute paths for executables in tests
- Subprocess call using partial executable path in test_release_script.py
- SC2181: check exit code directly in bump.sh

### Removed
- Devcontainer GitLab support
- src folder
- Validate/sync targets in rhiza repository

## [0.4.0] - 2025-12-26

### Added
- .rhiza folder for platform-agnostic CI/CD infrastructure

### Changed
- Updated TOKEN_SETUP.md path in rhiza_sync.yml
- Updated README with new test script descriptions
- Moving dependabot and renovate

### Fixed
- Typo in README.md

## [0.3.2] - 2025-12-25

### Added
- validate to the makefile interface
- Move .github/actions to .github/rhiza/actions folder
- Move workflow files to .github/workflows/ with rhiza_ prefix

### Changed
- Ensure correct rhiza version for sync
- Reorganize GitHub configuration under .github/rhiza namespace
- Improve make install

## [0.3.1] - 2025-12-24

### Added
- MakefileTools extension to devcontainer
- CONFIG.md to GitHub directory
- Comprehensive repository analysis with 9.0/10 rating
- PRESENTATION.md with Marp slides introducing the repository
- Dependabot configuration for automated dependency updates
- Benchmark target to Makefile.tests
- Fallback targets for book-related Make commands when book/ folder is missing
- README.md to presentation folder with Marp usage documentation
- Comprehensive Marimo showcase notebook

### Changed
- API docs improvements
- Test the structure and files with rhiza
- Filter workflow badges to main branch only
- Update badge links in README.md
- Split Makefile into modular components by functional area
- Refactor sync workflow by removing unnecessary steps
- Ignore benchmark folder by default when running make test
- Move benchmark init and update GitHub folder structure
- Folder structure improvements

### Fixed
- Version issues
- pdoc import failure when package metadata unavailable
- Sync workflow PR creation on scheduled runs
- Fix Marp server mode to accept directory instead of file

### Removed
- Remove the copier support
- Remove sync.sh existence check from tests

## [0.3.0] - 2025-12-16

### Added
- More comprehensive tests

### Changed
- Run in headless with no token
- Jazzup landing page

### Removed
- startup.sh
- src and dedicated test cli commands test

## [0.2.0] - 2025-12-16

### Added
- Materialize functionality

## [0.1.0] - 2025-12-16

### Added
- inject_rhiza.sh for automated repository integration

## [0.0.3] - 2025-12-16

### Removed
- addpy nonsense

## [0.0.2] - 2025-12-16

### Changed
- Initial release improvements

## [0.0.1] - 2025-12-16

### Added
- Initial release of rhiza (renamed from Config Templates)
- Reusable configuration templates for modern Python projects
- Logo and README updates
- Comprehensive integration guide for existing projects
- Extended available Templates
- Info for users

[Unreleased]: https://github.com/Jebel-Quant/rhiza/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/Jebel-Quant/rhiza/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/Jebel-Quant/rhiza/compare/v0.3.2...v0.4.0
[0.3.2]: https://github.com/Jebel-Quant/rhiza/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/Jebel-Quant/rhiza/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/Jebel-Quant/rhiza/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/Jebel-Quant/rhiza/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Jebel-Quant/rhiza/compare/v0.0.3...v0.1.0
[0.0.3]: https://github.com/Jebel-Quant/rhiza/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/Jebel-Quant/rhiza/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/Jebel-Quant/rhiza/releases/tag/v0.0.1
