import sqlite3

departments = {'Aero &amp; Astro Engineering': 'AAE', 'African American Studies': 'AAS', 'Agri &amp; Biol Engineering': 'ABE', 
              'Art &amp; Design': 'AD', 'Aerospace Studies': 'AFT', 'Agricultural Economics': 'AGEC', 'Agriculture': 'AGR', 'Agronomy': 'AGRY', 
              'American Studies': 'AMST', 'Animal Sciences': 'ANSC', 'Anthropology': 'ANTH', 'Arabic': 'ARAB', 'Asian American Studies': 'ASAM', 
              'Agric Sciences Educ &amp;Comm': 'ASEC', 'American Sign Language': 'ASL', 'Agricultural Systems Mgmt': 'ASM', 'Astronomy': 'ASTR', 
              'Aviation Technology': 'AT', 'Bands': 'BAND', 'Biochemistry': 'BCHM', 'Biological Sciences': 'BIOL', 'Biomedical Engineering': 'BME', 
              'Basic Medical Sciences': 'BMS', 'Botany &amp; Plant Pathology': 'BTNY', 'Candidate': 'CAND', 'Critical Disability Std': 'CDIS', 'Civil Engineering': 'CE', 
              'Construction Engr &amp; Mgmt': 'CEM', 'Computer Graphics Tech': 'CGT', 'Chemical Engineering': 'CHE', 'Chemistry': 'CHM', 'Chinese': 'CHNS', 'Classics': 'CLCS', 
              'Clinical Pharmacy': 'CLPH', 'Construction Management': 'CM', 'Comparative Literature': 'CMPL', 'Computer &amp; Info Tech': 'CNIT', 'Communication': 'COM', 'Comparative Pathobiology': 'CPB', 
              'Computer Sciences': 'CS', 'Consumer Science': 'CSR', 'Dance': 'DANC', 'Earth Atmos Planetary Sci': 'EAPS', 'Electrical &amp; Computer Engr': 'ECE', 'Electrical&amp;Comp Engr Tech': 'ECET', 
              'Economics': 'ECON', 'Educ-Curric &amp; Instruction': 'EDCI', "Educ-Ed'l and Psy Studies": 'EDPS', 'Ed Leadrship&amp;Cultrl Fnd': 'EDST', 'Environ &amp; Ecological Engr': 'EEE', 
              'Engineering Education': 'ENE', 'English': 'ENGL', 'Engineering': 'ENGR', 'Engineering Technology': 'ENGT', 'Entomology': 'ENTM', 'Entrepreneurship': 'ENTR', 'Engr Proj Cmity Service': 'EPCS', 
              'Forestry&amp;Natural Resources': 'FNR', 'French': 'FR', 'Food Science': 'FS', 'Film And Video Studies': 'FVS', 'Global Engineering Program': 'GEP', 'German': 'GER', 'Graduate Studies': 'GRAD', 
              'Greek': 'GREK', 'General Studies': 'GS', 'Global Studies Lib Arts': 'GSLA', 'Human Dev &amp; Family Sci': 'HDFS', 'Hebrew': 'HEBR', 'College Health &amp; Human Sci': 'HHS', 'History': 'HIST', 
              'Health And Kinesiology': 'HK', 'Honors': 'HONR', 'Horticulture': 'HORT', 'Health Sciences': 'HSCI', 'Hlth,Srvcs,Outcomes&amp;Polic': 'HSOP', 'Hospitality &amp; Tourism Mgmt': 'HTM', 
              'Interdisciplinary Engr': 'IDE', 'Interdisciplinary Studies': 'IDIS', 'Industrial Engineering': 'IE', 'Industrial Engr Technology': 'IET', 'Information &amp; Library Sci': 'ILS', 
              'Industrial &amp; Phys Pharm': 'IPPH', 'Industrial Technology': 'IT', 'Italian': 'ITAL', 'Japanese': 'JPNS', 'Jewish Studies': 'JWST', 'Korean': 'KOR', 'Landscape Architecture': 'LA', 
              'Latina Am&amp;Latino Studies': 'LALS', 'Latin': 'LATN', 'Languages and Cultures': 'LC', 'Linguistics': 'LING', 'Mathematics': 'MA', 'Med Chem &amp;Molecular Pharm': 'MCMP', 
              'Mechanical Engineering': 'ME', 'Mechanical Engr Tech': 'MET', 'Manufacturing Engr Tech': 'MFET', 'Management': 'MGMT', 'Materials Engineering': 'MSE', 'Military Science &amp; Ldrshp': 'MSL', 
              'Music History &amp; Theory': 'MUS', 'Natural Res &amp; Environ Sci': 'NRES', 'Naval Science': 'NS', 'Nuclear Engineering': 'NUCL', 'Nuclear Pharmacy': 'NUPH', 'Nursing': 'NUR', 
              'Nutrition Science': 'NUTR', 'Orgnztnl Bhvr &amp;Hum Resrce': 'OBHR', 'Organiz Ldrshp&amp;Supervision': 'OLS', 'Physical Education Skills': 'PES', 'Philosophy': 'PHIL', 'Pharmacy Practice': 'PHPR', 
              'Pharmacy': 'PHRM', 'Physics': 'PHYS', 'Political Science': 'POL', 'Psychological Sciences': 'PSY', 'Portuguese': 'PTGS', 'Public Health': 'PUBH', 'Reg File Maintenance': 'REG', 'Religious Studies': 'REL', 
              'Russian': 'RUSS', 'General Science': 'SCI', 'Studies Coll Liberal Arts': 'SCLA', 'Sustainable Food&amp;Farm Sys': 'SFS', 'Speech, Lang&amp;Hear Science': 'SLHS', 'Sociology': 'SOC', 'Spanish': 'SPAN', 
              'Statistics': 'STAT', 'Purdue Sys Collaboratory': 'SYS', 'The Data Mine': 'TDM', 'Technology': 'TECH', 'Theatre': 'THTR', 'Technology Ldrshp Innovatn': 'TLI', 'Veterinary Clinical Sci': 'VCS', 
              'Vertically Integrated Proj': 'VIP', 'Veterinary Medicine': 'VM', 'Women Gend&amp;Sexuality Std': 'WGSS'}

# Connect to DB and create a cursor
db = sqlite3.connect('instance/database.db')
c = db.cursor()
print('DB Init')

for d in departments.keys():
    c.execute('INSERT INTO department (department, department_code) VALUES (?, ?)', (d, departments[d]))
    db.commit()
 
# Close the cursor
c.close()