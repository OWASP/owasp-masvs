# OWASP ASVS 3.0 in Markdown

This is a proof of concept to show that the OWASP ASVS could be developed and managed in the Markdown format. See the original discussion here https://github.com/OWASP/ASVS/issues/99

This is not the official OWASP ASVS Github Repository, the official one is here https://github.com/OWASP/ASVS

Why use Markdown? Here is one of many blog posts online which explains the benefits http://ben.balter.com/2012/10/19/we-ve-been-trained-to-make-paper/#jailbreaking-content

## Convert .docx to .md

```
gem install word-to-markdown
w2m "OWASP\ Application\ Security\ Verification\ Standard\ 3.0.docx" > asvs.md
```

Then remove the base64 data images to keep size down.

Thanks to the incredibly awesome [word-to-markdown](https://github.com/benbalter/word-to-markdown) Ruby gem!

## Convert Markdown to other formats

Markdown can be converted to a multitude of different formats. There are many free / Open Source converters which can be found online.

## Future Suggestions

1. Use continuous integration to run things like spell checkers - https://travis-ci.org/
2. Split each chapter or section into its own file.
3. Create a commit hook to join all the separate chapters/sections into 1 file for consumption.
