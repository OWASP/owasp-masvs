VERSION := 1.2
CHAPTERS := Document/0x*.md Document/CHANGELOG.md

# Run and destroy a dalibo/pandocker (masvs-generator) container with the current directory mounted at /pandoc
PANDOC := docker run --rm -u `id -u`:`id -g` -v ${PWD}:/pandoc masvs-generator
# PANDOC := docker run --rm -u `id -u`:`id -g` -v `pwd`:/pandoc dalibo/pandocker # FOR LOCAL

# For pandoc, give the Documents folder as resource-path and we use xelatex as PDF engine
# Uses eisvogel as template: https://github.com/Wandmalfarbe/pandoc-latex-template/blob/master/eisvogel.tex
OPTS_ALL := --resource-path=.:Document --pdf-engine=xelatex --template=eisvogel

# Include a ToC with the title "Table of Contents" and a depht of 1.
# We tweak the current template with the options included in latex-header.tex
# Override link colors in blue and include the cover as the first page
OPTS_DOC_ALL := --toc -V toc-title:"Table of Contents" --toc-depth=1 -H latex-header.tex -V linkcolor:blue --include-before-body Document/cover.tex --include-before-body Document/first_page.tex

all: OWASP_MASVS-SNAPSHOT.pdf

OWASP_MASVS-SNAPSHOT.pdf: $(CHAPTERS) Makefile
	sed -i 's/MASVS_VERSION/$(VERSION)/g' Document/first_page.tex
	$(PANDOC) 'pandoc $(OPTS_ALL) $(OPTS_DOC_ALL) -o $@ $(CHAPTERS)'
	# $(PANDOC) $(OPTS_ALL) $(OPTS_DOC_ALL) -o $@ $(CHAPTERS)
	# FOR LOCAL 

clean:
	rm OWASP_MASVS-SNAPSHOT.pdf