VERSION := 1.2
LANGUAGE := "" #(Japanese Version)
CHAPTERS := Document/0x*.md Document/CHANGELOG.md


# Run and destroy a dalibo/pandocker (masvs-generator) container with the current directory mounted at /pandoc
PANDOC := docker run --rm -u `id -u`:`id -g` -v ${PWD}:/pandoc masvs-generator
# PANDOC := docker run --rm -u `id -u`:`id -g` -v `pwd`:/pandoc dalibo/pandocker # FOR LOCAL

# For pandoc, give the Documents folder as resource-path and we use xelatex as PDF engine
# Uses eisvogel as template: https://github.com/Wandmalfarbe/pandoc-latex-template/blob/master/eisvogel.tex
OPTS_ALL := --pdf-engine=xelatex --template=eisvogel

# Include a ToC with the title "Table of Contents" and a depht of 1.
# We tweak the current template with the options included in latex-header.tex
# Override link colors in blue and include the cover as the first page
OPTS_DOC_ALL := --toc -V toc-title:"Table of Contents" --toc-depth=1 -H latex-header.tex -V linkcolor:blue --include-before-body tmp_cover.tex --include-before-body tmp_first_page.tex

all: OWASP_MASVS-SNAPSHOT.pdf

OWASP_MASVS-SNAPSHOT.pdf:
	sed -e "s/{{MASVS-VERSION}}/$(VERSION)/g" first_page.tex > tmp_first_page.tex
	sed -e "s/{{MASVS-VERSION}}/$(VERSION)/g" -e "s/{{MASVS-LANGUAGE}}/$(LANGUAGE)/g" cover.tex > tmp_cover.tex
	
	$(PANDOC) 'pandoc --resource-path=.:Document $(OPTS_ALL) $(OPTS_DOC_ALL) -o $@ $(CHAPTERS)'
# $(PANDOC) --resource-path=.:Document $(OPTS_ALL) $(OPTS_DOC_ALL) -o $@ $(CHAPTERS)
# FOR LOCAL 
	rm tmp_first_page.tex
	rm tmp_cover.tex

clean:
	rm OWASP_MASVS-SNAPSHOT.pdf