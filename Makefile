# Makefile for Sphinx documentation
#
SHELL         = /bin/bash
BUILDDIR			= build
STATICDIR			= src/nginx-sphinx/static

.PHONY: help clean 

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf $(STATICDIR)/css/*
	rm -rf $(STATICDIR)/js/*

prep: 
	@echo "Copying assets from f5-hugo"
	$(shell if ! [ -d "f5-hugo/assets" ] ; then\
		git submodule update --init f5-hugo ; \
	fi)
	$(shell cp -R f5-hugo/assets/js/ $(STATICDIR)/js/)
	$(shell cp -R f5-hugo/assets/css/ $(STATICDIR)/css/) 
	




