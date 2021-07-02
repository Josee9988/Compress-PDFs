<!-- markdownlint-disable MD032 MD033-->
# 📦 **Josee9988/Compress-PDFs**

<div align="center">
  <a href="https://github.com/Josee9988/Compress-PDFs/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/Josee9988/Compress-PDFs?color=0088ff&style=for-the-badge&logo=github"/>
  </a>
  <a href="https://github.com/Josee9988/Compress-PDFs/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/Josee9988/Compress-PDFs?color=0088ff&style=for-the-badge&logo=github"/>
  </a>
</div>

---

## 🤔 **About the project**

* A CLI tool to compress 📦 all PDFs recursively in a directory.

---

## ⚡ **Installation**

1. Clone the repository and `cd` into it

2. *Install pip3*

    ```bash
    sudo apt install python3-pip
    # verify it with pip3 --version
    ```

3. Instal the ilovepdf dependency

    ```bash
    pip3 install pylovepdf
    ```

4. Make the script executable from anywhere

    ```bash
    bash MAKE_SCRIPT_GLOBAL.sh
    ```

5. Rename `.env.example` to `.env`.

    ```bash
    mv -v .env.example .env # rename to .env
    ```

6. Add your [IlovePDF](https://developer.ilovepdf.com/) public key

    * Modify the `.env` file add update the **`PUBLIC_KEY`** variable with your public key from [the IlovePDF developer's site](https://developer.ilovepdf.com/)

7. Run it ;)

    ```bash
    python3 compress.py /PATH/TO/YOUR/DIR/
    ```

---

## 🚀 **Usage**

* After running the script `MAKE_SCRIPT_GLOBAL.sh` you can call the script from anywhere in your system with: `python3 compress.py`

* The script receives only one argument and it is the path of the directory that will be recursively compressed. All the subfolders will be looked up to compress all the pdfs inside the passed directory.

* Script profile

  ```bash
  python3 compress.py <Directory path>
  ```

---

## 🌲 **Project tree**

```bash
.
├── compress.py
├── .env.example
├── .github
│   ├── CODE_OF_CONDUCT.md
│   ├── CODEOWNERS
│   ├── config.yml
│   ├── CONTRIBUTING.md
│   ├── FUNDING.yml
│   ├── issue_label_bot.yaml
│   ├── ISSUE_TEMPLATE
│   │   ├── 1-bug-report.md
│   │   ├── 2-failing-test.md
│   │   ├── 3-docs-bug.md
│   │   ├── 4-feature-request.md
│   │   ├── 5-enhancement-request.md
│   │   ├── 6-security-report.md
│   │   ├── 7-question-support.md
│   │   └── config.yml
│   ├── ISSUE_TEMPLATE.md
│   ├── pull_request_template.md
│   ├── SECURITY.md
│   ├── settings.yml
│   └── SUPPORT.md
├── .gitignore
├── LICENSE
├── MAKE_SCRIPT_GLOBAL.sh
└── README.md

2 directories, 25 files
```

---

## 📝 **Additional notes**

* In case an error happens because there are multiple pdfs with the same name or simply the program doesn't know how to replace them, an error will be prompt and you will have to manually move the compressed pdf (which will be in the directory passed as an argument) to the desired directory.
* The cloned repository should not be  removed as it contains the symbolic link which is globally executable. You can manually move the file and the .env file to your /bin/ folder if you wish.

---

Compress-PDFs was generated from *[Josee9988/project-template](https://github.com/Josee9988/project-template)* 📚

---

🕵️ Extra recommendations

* Always check the console output to check if any error happened and if so, you will have to manually move the non-moved compressed file to its location.

* Also always perform a copy of the folder before using the script as it will remove the old PDFs and it might cause some data loss if an error occurs.

---

## 🎉 Was the pdf compressor helpful? Help us raise these numbers up

[![Github followers](https://img.shields.io/github/followers/Josee9988.svg?style=social)](https://github.com/Josee9988)
[![Github stars](https://img.shields.io/github/stars/Josee9988/Compress-PDFs.svg?style=social)](https://github.com/Josee9988/Compress-PDFs/stargazers)
[![Github watchers](https://img.shields.io/github/watchers/Josee9988/Compress-PDFs.svg?style=social)](https://github.com/Josee9988/Compress-PDFs/watchers)
[![Github forks](https://img.shields.io/github/forks/Josee9988/Compress-PDFs.svg?style=social)](https://github.com/Josee9988/Compress-PDFs/network/members)
<!-- MODIFY THIS LINK TO YOUR MAIN DONATING SITE IF YOU ARE NOT IN THE GITHUB SPONSORS PROGRAM -->
[![Sponsor](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=github-sponsors&color=red&style=social)](https://github.com/sponsors/Josee9988)

Enjoy! 😃

---

## ⚖️📝 **License**

See the license in the '**[LICENSE](LICENSE)**' file.

---

_Made with a lot of ❤️❤️ by **[@Josee9988](https://github.com/Josee9988)**_
