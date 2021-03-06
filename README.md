<!-- markdownlint-disable MD032 MD033-->
# ð¦ **Josee9988/Compress-PDFs**

<div align="center">
  <a href="https://github.com/Josee9988/Compress-PDFs/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/Josee9988/Compress-PDFs?color=0088ff&style=for-the-badge&logo=github"/>
  </a>
  <a href="https://github.com/Josee9988/Compress-PDFs/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/Josee9988/Compress-PDFs?color=0088ff&style=for-the-badge&logo=github"/>
  </a>
</div>

â ï¸This project is not fully finished or tester, it might cause some errors with in certain situations. Please, do a backup of the folders you want to compress before using this script.â ï¸

---

## ð¤ **About the project**

* A CLI tool to compress ð¦ all PDFs recursively in a directory.

---

## â¡ **Installation**

1. Clone the repository and `cd` into it

    ```bash
    git clone git@github.com:Josee9988/Compress-PDFs.git && cd Compress-PDFs
    ```

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
    compress.py /RELATIVE/OR/ABSOLUTE/PATH/TO/YOUR/DIR/
    ```

---

## ð **Usage**

* After running the script `MAKE_SCRIPT_GLOBAL.sh` you can call the script from anywhere in your system with: `compress.py <path>`

* The script receives only one argument and it is the path of the directory that will be recursively compressed. All the subfolders will be looked up to compress all the pdfs inside the passed directory as an argument.

* Script profile

  ```bash
  compress.py <Directory path>
  ```

* Some examples of usage

  1. Using an absolute path

      ```bash
      compress.py /home/username/Documents/MyFolder
      ```

  2. Using a relative path

      ```bash
      compress.py .
      ```

      ```bash
      compress.py /dirFromWhereIAm/whatever/
      ```

---

## ð² **Project tree**

```bash
.
âââ compress.py
âââ .env
âââ .github
â   âââ CODE_OF_CONDUCT.md
â   âââ CODEOWNERS
â   âââ config.yml
â   âââ CONTRIBUTING.md
â   âââ FUNDING.yml
â   âââ issue_label_bot.yaml
â   âââ ISSUE_TEMPLATE
â   â   âââ 1-bug-report.md
â   â   âââ 2-failing-test.md
â   â   âââ 3-docs-bug.md
â   â   âââ 4-feature-request.md
â   â   âââ 5-enhancement-request.md
â   â   âââ 6-security-report.md
â   â   âââ 7-question-support.md
â   â   âââ config.yml
â   âââ ISSUE_TEMPLATE.md
â   âââ pull_request_template.md
â   âââ SECURITY.md
â   âââ settings.yml
â   âââ SUPPORT.md
âââ .gitignore
âââ LICENSE
âââ MAKE_SCRIPT_GLOBAL.sh
âââ README.md

2 directories, 25 files
```

---

## ð **Additional notes**

* The compressed PDF's will automatically replace your old and uncompressed ones.
* In case an error happens because there are multiple pdfs with the same name or simply the program doesn't know how to replace them, an error will be prompt and you will have to manually move the compressed pdf (which will be in the directory passed as an argument) to the desired directory.
* The cloned repository should not be  removed as it contains the symbolic link which is globally executable. You can manually move the file and the .env file to your /bin/ folder if you wish.

---

Compress-PDFs was generated from *[Josee9988/project-template](https://github.com/Josee9988/project-template)* ð

---

## ðµï¸ Extra recommendations

* Always check the console output to check if any error happened and if so, you will have to manually move the non-moved compressed file to its location.

* Also, always perform a copy of the folder before using the script as it will remove the old PDFs, and it might cause some data loss if an error occurs.

---

## ð Was the pdf compressor helpful? Help us raise these numbers up

[![Github followers](https://img.shields.io/github/followers/Josee9988.svg?style=social)](https://github.com/Josee9988)
[![Github stars](https://img.shields.io/github/stars/Josee9988/Compress-PDFs.svg?style=social)](https://github.com/Josee9988/Compress-PDFs/stargazers)
[![Github watchers](https://img.shields.io/github/watchers/Josee9988/Compress-PDFs.svg?style=social)](https://github.com/Josee9988/Compress-PDFs/watchers)
[![Github forks](https://img.shields.io/github/forks/Josee9988/Compress-PDFs.svg?style=social)](https://github.com/Josee9988/Compress-PDFs/network/members)
[![Sponsor](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=github-sponsors&color=red&style=social)](https://github.com/sponsors/Josee9988)

Enjoy! ð

---

## âï¸ð **License**

See the license in the '**[LICENSE](LICENSE)**' file.

---

_Made with a lot of â¤ï¸â¤ï¸ by **[@Josee9988](https://github.com/Josee9988)**_
