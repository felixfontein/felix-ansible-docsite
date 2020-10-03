# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = rst
BUILDDIR      = build

COLLECTION_LIMIT = --limit felixfontein.tools --limit felixfontein.hosttech_dns --limit community.sops --limit community.crypto

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" -c . $(SPHINXOPTS) $(O)

build_modules:
	rm -rf temp-rst
	mkdir -p temp-rst
	antsibull-docs current --dest-dir temp-rst $(COLLECTION_LIMIT)
	rsync -avc --delete-after temp-rst/collections/ rst/collections/

html_complete: build_modules html
	#

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c . $(SPHINXOPTS) $(O)
