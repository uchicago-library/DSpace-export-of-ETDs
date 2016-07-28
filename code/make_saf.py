
import csv
from os import scandir, path, mkdir
from sys import stderr, stdout
from xml import etree
from xml.etree import ElementTree as ET
import re
import shutil

directory = "X:/ETDs"

contents = scandir(directory)

saf_path_root = "C:/Users/tdanstrom/Documents/etds_safs/"

def make_dublin_core_xml(title_value, author_value, date_value):
    root = ET.Element("dublin_core")
    title = ET.SubElement(root, 'dcvalue')
    author = ET.SubElement(root, 'dcvalue')
    title.set('element', 'title')
    title.set('qualifier', 'none')
    date = ET.SubElement(root, 'dcvalue')
    date.set('element', 'date')
    date.set('qualifier', 'issued')
    author.set('element', 'creator')
    author.set('qualifier', 'none')
    title.text = title_value.decode(encoding='utf-8')
    author.text = author_value
    date.text = date_value
    return root

def make_etd_metadata(department_value, degree_level_value, degree_institution):
    root = ET.Element("dublin_core")
    root.set('schema', 'etd')
    degree_dept = ET.SubElement(root, 'dcvalue')
    degree_level = ET.SubElement(root, 'dcvalue')
    degree_grantor = ET.SubElement(root, 'dcvalue')
    degree_dept.set('element', 'degree')
    degree_dept.set('qualifier', 'department')
    degree_level .set('element', 'degree')
    degree_level.set('qualifier', 'level')
    degree_grantor.set('element', 'degree')
    degree_grantor.set('qualifier', 'grantor')
    degree_grantor.text = degree_institution
    degree_level.text = degree_level_value
    degree_dept.text = department_value
    return root

for n in contents:
    if n.is_dir() and n.name.startswith('etdadmin'):
        cur_path = n.path
        saf_identifier = re.compile('(etdadmin_upload_\d{6})').search(n.name).group(1)
        saf_path = path.join(saf_path_root, saf_identifier)
        if not(path.exists(saf_path)):
            mkdir(saf_path)
        dept_collection = None
        subject_collection = "Theses and Dissertations"
        collections = []
        collections.append(subject_collection)
        contents = []
        for p in scandir(cur_path):
            if p.name.endswith('xml'):
                xml_doc = ET.parse(p.path)
                xml_root = xml_doc.getroot()
                title = xml_root.find("DISS_description/DISS_title").text.encode('utf-8')
                author_fname = xml_root.find("DISS_authorship/DISS_author[@type='primary']/DISS_name/DISS_fname").text
                author_surname = xml_root.find("DISS_authorship/DISS_author[@type='primary']/"+"DISS_name/DISS_surname").text
                author = author_fname + ' ' + author_surname
                comp_date = xml_root.find("DISS_description/DISS_dates/DISS_comp_date").text
                dept_collection = xml_root.find("DISS_description/DISS_institution/DISS_inst_contact").text
                inst_degree_level = xml_root.find("DISS_description/DISS_degree").text
                inst_grantor = xml_root.find("DISS_description/DISS_institution/DISS_inst_name").text
                collections.append(dept_collection)
                dc_node = make_dublin_core_xml(title, author, comp_date)
                etd_node = make_etd_metadata(dept_collection, inst_degree_level, inst_grantor)

                etd_filepath = path.join(saf_path, 'metadata_etd.xml')
                dublincore_filepath = path.join(saf_path, 'dublin_core.xml')
                contents.append(path.basename(etd_filepath))
                contents.append(path.basename(dublincore_filepath))

                etd_tree = ET.ElementTree(etd_node)
                dublincore_tree = ET.ElementTree(dc_node)

                etd_tree.write(etd_filepath, encoding='utf-8', xml_declaration=True)
                dublincore_tree.write(dublincore_filepath, encoding='utf-8', xml_declaration=True)

                print(dc_node)
                print(etd_node)

            if p.name.endswith('.pdf'):
                contents.append(p.name)
                shutil.copy(p.path, saf_path)

        collections_filepath = path.join(saf_path, 'collections.txt')
        contents_filepath = path.join(saf_path, 'contents.txt')
        opened_collections = open(collections_filepath, 'w')
        opened_contents= open(contents_filepath, 'w')
        opened_collections.write("\n".join(collections))
        opened_contents.write("\n".join(contents))
