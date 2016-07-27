import csv
from os import scandir
from sys import stderr, stdout
from xml.etree import ElementTree as ET

directory = "X:/ETDs"

contents = scandir(directory)

count = 0
all_lines = []
for n in contents:
    if n.is_dir() and n.name.startswith('etdadmin'):
        cur_path = n.path
        for p in scandir(cur_path):
            if p.name.endswith('.xml'):
                xml_doc = ET.parse(p.path)
                xml_root = xml_doc.getroot()
                # title = ""
                # author = ""
                # date = ""
                # license = ""
                try:
                    title = xml_root.find("DISS_description/DISS_title")
                    author_first_name = xml_root.find("DISS_authorship/DISS_author[@type='primary']/DISS_name/DISS_fname")
                    author_surname = xml_root.find("DISS_authorship/DISS_author[@type='primary']/DISS_name/DISS_surname")
                    inst_contact = xml_root.find("DISS_description/DISS_institution/DISS_inst_contact")


                    comp_date = xml_root.find("DISS_description/DISS_dates/DISS_comp_date")

                    license = xml_root.find("DISS_creative_commons_license/DISS_abbreviation")
                    acceptance = xml_root.find("DISS_repository/DISS_acceptance")
                    try:
                        acceptance_text = acceptance.text
                    except:
                        acceptance_text = 'null'
                    try:
                        license_text = license.text.encode('utf-8')
                        title = title.text.encode('utf-8')
                        author_fname = author_first_name.text.encode('utf-8')
                        author_sname = author_surname.text.encode('utf-8')
                        author = author_fname + b" " + author_sname
                        comp_date = comp_date.text.encode('utf-8')
                        inst_contact = inst_contact.text.encode('utf-8')
                        line = [title,author,comp_date,inst_contact,license_text.strip(),acceptance_text.encode('utf-8').strip()]
                        all_lines.append(line)
                        count += 1
                    except:
                        pass
                except:
                    stderr.write("{} cannot be read\n".format(p.path))

with open("X:\ETDS\pots.csv","w") as writingfile:
    spamwriter = csv.writer(writingfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

  
    for line in all_lines:
        print(line)
        print(type(line))
        spamwriter.writerow(line)

  # <DISS_repository>
  #   <DISS_version/>
  #   <DISS_agreement_decision_date/>
  #   <DISS_acceptance>0</DISS_acceptance>

##with open('X:\ETDS\pot_licensed.csv', 'w') as csvfile:
    #pot_licensed_writer = csv.writer(csvfile, delimiter=',',
    #                        quotechar='"', quoting=csv.QUOTE_ALL)

print(len(all_lines))
print(count)
print("There are {} total valid disserattions".format(str(count)))

# <DISS_description page_count="262" type="doctoral" external_id="http://dissertations.umi.com/uchicago:13029" apply_for_copyright="no">
#     <DISS_title>The Internet Effect: How Authoritarian Governments Use Internet Communications Technologies to Maintain Control of States</DISS_title>
#     <DISS_dates>
#       <DISS_comp_date>2015-08</DISS_comp_date>
#       <DISS_accept_date>01/01/2015</DISS_accept_date>
#     </DISS_dates>
#     <DISS_degree>Ph.D.</DISS_degree>
#     <DISS_institution>
#       <DISS_inst_code>0330</DISS_inst_code>
#       <DISS_inst_name>The University of Chicago</DISS_inst_name>
#       <DISS_inst_contact>Political Science</DISS_inst_contact>

        # <DISS_surname>Benson</DISS_surname>
        # <DISS_fname>David</DISS_fname>
        # <DISS_middle>Carl</DISS_middle>
    # <DISS_dates>
    #   <DISS_comp_date>2015-08</DISS_comp_date>

#   <DISS_authorship>
#     <DISS_author type="primary">
#       <DISS_name>
#         <DISS_surname>Hund</DISS_surname>
#         <DISS_fname>Zachary</DISS_fname>
#         <DISS_middle>Michael</DISS_middle>
#         <DISS_suffix/>
#         <DISS_affiliation>University of Chicago</DISS_affiliation>
#       </DISS_name>


# <DISS_submission publishing_option="0" embargo_code="4" third_party_search="N">
#   <DISS_description page_count="243" type="doctoral" external_id="http://dissertations.umi.com/uchicago:13030" apply_for_copyright="no">
#     <DISS_title>Atomic Scattering from Methyl-Terminated Si and Ge</DISS_title>
#     <DISS_dates>
#       <DISS_comp_date>2015-08</DISS_comp_date>
#       <DISS_accept_date>01/01/2015</DISS_accept_date>
#     </DISS_dates>

#  <DISS_content>
#     <DISS_abstract>
#       <DISS_para>This thesis describes the investigations we have conducted into the effects of organic functionalization on the atomic surface structure, vibrational dynamics, and vibrational band structure of crystalline semiconductors.  Specifically, we have studied rather novel surfaces that arise from methyl termination of silicon(111) and germanium(111) semiconductor lattices.  We employed helium atom scattering to examine both of these functionalized surfaces, as this specific technique is a completely surface-sensitive, non-destructive probe of the methyl interface.  The surface structure and vibrational dynamics, including atomic spacings, step heights, average atomic displacements, potential well depths, and Debye temperatures, were all measured via the elastic diffraction of helium atoms from the surface.  Inelastic time-of-flight measurements resolved the energy exchanges between colliding helium atoms and lattice vibrations; taking these measurements at a variety of kinematic conditions allowed us to map out the evolution of phonons (e.g. the Rayleigh wave) across the surface Brillouin zone.  Switching to a hydrogen and deuterium molecular beam produced diffraction spectra with highly-resolved rotationally inelastic diffraction peaks; the anisotropy of the surface can be estimated from these rotational excitations.  High-level density functional theory and molecular dynamics simulations were completed in conjunction with the atomic scattering measurements to further our understanding of how, specifically, methyl termination of these Si(111) and Ge(111) semiconductors affects their dynamics and band structure.</DISS_para>
#     </DISS_abstract>
#     <DISS_binary type="PDF">Hund_uchicago_0330D_13030.pdf</DISS_binary>
#   </DISS_content

