# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = rst
BUILDDIR      = build

COLLECTIONS   = felixfontein.acme felixfontein.hosttech_dns felixfontein.tools community.crypto community.dns community.docker community.hrobot community.routeros community.sops

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" -c . $(SPHINXOPTS) $(O)
	@echo -e 'Additional targets: \x1B[97mbuild_modules\x1B[0m, \x1B[97mhtml_complete\x1B[0m'

build_modules:
	rm -rf temp-rst
	mkdir -p temp-rst
	antsibull-docs collection --use-current --dest-dir temp-rst $(COLLECTIONS)
	rsync -avc --delete-after temp-rst/collections/ rst/collections/

html_complete: build_modules html
	#

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -c . $(SPHINXOPTS) $(O)
