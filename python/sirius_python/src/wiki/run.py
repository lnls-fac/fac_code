#!/usr/bin/python

import os
import pywikibot
import storage_ring
import booster


bot_default_comment = 'Automatically generated by '+os.path.basename(__file__)


def check_deps(parameters):

    names = [parameter.name for parameter in parameters]
    for parameter in parameters:
        msg = ''
        deps = parameter.deps
        for dep in deps:
            if dep not in names:
                if msg is '':
                    msg = str(parameter.name) + ': ' + str(dep)
                else:
                    msg += ', ' + str(dep)

        if msg is not '':
            print(msg)


def generate_parameter_name_list_page(label, parameters):
    
    wiki = []
    for parameter in parameters:
        wiki.append('#[[Parameter:' + parameter.name + '|' + parameter.name + ']]')
    
    site = pywikibot.Site('en', 'siriuswiki')
    page = pywikibot.Page(site, 'DDR:' + label + ' parameter name list')
    page.text = '\n'.join(wiki)
    page.save(bot_default_comment)
    
    
def generate_parameter_pages(parameters):
    site = pywikibot.Site('en', 'siriuswiki')  
    for parameter in parameters:
        page = pywikibot.Page(site, 'Parameter:'+parameter.name)
        page.text = parameter.create_wiki_page()
        page.save(bot_default_comment)

    
#check_deps(sirius_sr)
#generate_parameter_pages(storage_ring.parameter_list)
generate_parameter_name_list_page(storage_ring.label, storage_ring.parameter_list)