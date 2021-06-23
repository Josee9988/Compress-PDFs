<!-- markdownlint-disable MD024-->
# **Change Log** 📜📝

All notable changes to the "**Project template**" repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [**1.7.0**] - 2021-06-01

### Added

* Type: Test issue label.
* Failing test issue template adds the new Type Test issue label.
* Updated README.md with the new label.

## [**1.6.0**] - 2021-05-21

### Added

* Divided the feature request into feature and enhancement request, each one with its respective labels.

### Changed

* Position of disclaimers and comments in the issue templates are moved to the bottom (but the security report) as some users directly erased everything to not read the text.
* Image of the issue templates in the readme.md file.

## [**1.5.0**] - 2021-05-15

### Added

* Auto-detection of user email.

## [**1.4.5**] - 2021-04-24

### Added

* Sponsor section in the project's main readme.md file.
* Improved and added documentation in the scripts.

### Fixed

* Readme "What does it include" fixed list of files.
* Sponsor link in the generated README.md file.
* Some typos

## [**1.4.4**] - 2021-04-22

### Added

* --help option in the script.
* More documentation and information for the user in the script prompts

## [**1.4.3**] - 2021-04-21

### Added

* Support for Github todo app.

## [**1.4.2**] - 2021-04-20

### Added

* An extra informational message in the script.
* Welcome bot and its config (.github/config.yml)

### Fixed

* Issue templates now auto assigns the new labels.

## [**1.4.1**] - 2021-04-20

### Added

* Security label

### Changed

* Project tree to its updated version.

## [**1.4.0**] - 2021-04-19

### Added

* Readme file with the section with the recommended/used bots that the users should install.
* Some informational comments in the script referencing the project's documentation.
* A total of 18 new labels will be created right when you clone your repo using Github Probot settings.

## [**1.3.0**] - 2021-04-14

### Added

* CODEOWNERS file inside the .github folder.

### Fixed

* Some README.md markdownlint bugs.

## [**1.2.0**] - 2021-04-07

### Added

* Bug report issue templates have the preceding "[BUG]" title.
* Multiple readme template headings (About the project, project tree, screenshots, donators).
* Improved README.md template by fixing some minor problems.

## [**1.1.1**] - 2021-04-02

### Added

* Username and project name are automatically selected (user can manually force change them using bash parameters [Username] [Project-Name])

### Changed

* Asciinema video

## [**1.1.0**] - 2021-03-31

### Added

* Gitignore file ignores all \*.ignore.\* files.
* Basic README.md template.
* bin/FUNCTION_HELPERS script to improve the readability of the SETUP_TEMPLATE.sh file.

### Changed

* Header's emoji from the end of the README.md headers to the beginning to be shown better by the new GitHub's README table of contents.

### Fixed

* Git status is shown before the commit.

### Fixed

* Some typos in the CHANGELOG.md.

## [**1.0.11**] - 2021-03-20

### Added

* Social links of the repo in the README.md file.
* Added badges in the README.md file.
* Added sponsor link in the contributing.yml file.

### Fixed

* Some minor typos in the README.md file.

## [**1.0.10**] - 2021-03-17

### Changed

* `EXECUTEME.sh` script changed to `SETUP_TEMPLATE.sh`.
* Changed the execution video from the README.md file (Asciinema's video).

## [**1.0.9**] - 2021-03-17

### Added

* The script will git add and commit the new files/changes for you.

## [**1.0.8**] - 2021-03-17

### Changed

* Improved README.md structure and fixed some typos.

### Added

* 'Extra recommendations' section in the README.md file.

## [**1.0.7**] - 2021-03-16

### Fixed

* Some minor typos

## [**1.0.6**] - 2021-03-16

### Changed

* Simplified PR template to make it easier.

## [**1.0.5**] - 2021-03-13

### Added

* Checks to the shell script (check if the files exist)
* Colourized the output of the script.

## [**1.0.4**] - 2021-02-26

### Added

* Markdownlint disable the rule in the CHANGELOG.md file"

## [**1.0.3**] - 2021-02-23

### Removed

* Josee's funding links.

### Added

* Shell script now checks if the .github directory exists.

## [**1.0.2**] - 2020-09-08

### Added

* One more screenshot to the README.md file showing the community profile.
* Documentation for the SETUP_TEMPLATE.sh script.

### Changed

* The project tree view showing the new LICENSE file.

## [**1.0.1**] - 2020-09-08

### Added

* A LICENSE for the project will be removed with the SETUP_TEMPLATE.sh script.

### Changed

* The location of the pull request template to the .github/ folder.

## [**1.0.0**] - 2020-09-08

### Added

* Added a CHANGELOG.md.
* Support for the CHANGELOG in the SETUP_TEMPLATE.sh file (when run, it will remove all of the content and create a new file from scratch).
