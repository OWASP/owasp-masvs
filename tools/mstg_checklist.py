import xlsxwriter
import i18n
from os import listdir
from os.path import isfile, join
import re


def createchecklist(masvs, lang):
    i18n.load_path.append('translations/')
    i18n.set('filename_format', 'checklist.json')
    i18n.set('locale', lang)

    if lang == "en":
        mypath = '../Document'
    else:
        mypath = '../Document-' + lang

    workbook = xlsxwriter.Workbook('../Generated/Mobile_App_Security_Checklist-' + lang + '.xlsx')

    # Worksheet 'Dashboard'
    workbook.add_worksheet(i18n.t('Dashboard.worksheet'))

    # Worksheet 'Management Summary'
    workbook.add_worksheet(i18n.t('ManagementSummary.worksheet'))

    # Worksheet 'Security Requirements - Android'
    workingsheet = workbook.add_worksheet(i18n.t('SecurityRequirementsAndroid.worksheet'))
    # Title
    workingsheet.write(0, 1, i18n.t('SecurityRequirementsAndroid.title'))
    # Table Header
    workingsheet.write(2, 1, i18n.t('SecurityRequirementsAndroid.ID'))
    workingsheet.write(2, 2, i18n.t('SecurityRequirementsAndroid.MSTG-ID'))
    workingsheet.write(2, 3, i18n.t('SecurityRequirementsAndroid.DetailedVerificationRequirement'))
    workingsheet.write(2, 4, i18n.t('SecurityRequirementsAndroid.Level1'))
    workingsheet.write(2, 5, i18n.t('SecurityRequirementsAndroid.Level2'))
    workingsheet.write(2, 6, i18n.t('SecurityRequirementsAndroid.Status'))

    # Worksheet 'Anti-RE - Android'
    workingsheet = workbook.add_worksheet(i18n.t('Anti-REAndroid.worksheet'))
    # Title
    workingsheet.write(0, 1, i18n.t('Anti-REAndroid.title'))
    # Table Header
    workingsheet.write(2, 1, i18n.t('Anti-REAndroid.ID'))
    workingsheet.write(2, 2, i18n.t('Anti-REAndroid.MSTG-ID'))
    workingsheet.write(2, 3, i18n.t('Anti-REAndroid.ResiliencyAgainstReverseEngineeringRequirements'))
    workingsheet.write(2, 4, i18n.t('Anti-REAndroid.R'))
    workingsheet.write(2, 5, i18n.t('Anti-REAndroid.Status'))

    # Worksheet 'Security Requirements - iOS'
    workingsheet = workbook.add_worksheet(i18n.t('Security Requirements - iOS'))

    # Worksheet 'Anti-RE - iOS'
    workingsheet = workbook.add_worksheet(i18n.t('Anti-RE - iOS'))

    # Worksheet 'Version history'
    workingsheet = workbook.add_worksheet(i18n.t('Version history'))

    workingsheet = workbook.get_worksheet_by_name(i18n.t('Security Requirements - Android'))
    row = 3
    # Parse each category
    onlyfiles = [filename for filename in listdir(mypath) if isfile(join(mypath, filename))]
    for filename in sorted(onlyfiles):
        # if file is category file
        match = re.search(r'0x\d{2}\-(V\d+)\-(.*)\.md', filename)
        if match and match.group(1) != 'V8':
            with open(join(mypath, filename)) as file:
                datafile = file.readlines()

            for line in datafile:
                match = re.search(r'\|\s\*\*(\d\.\d+)\*\*\s\|\s(\w+‑\w+‑\d+)\s\|\s(.*)\s\|\s?(\s✓|\s)\s\|\s(✓|\s)\s\|',
                                  line)
                if match:
                    workingsheet.write(row, 1, match.group(1))
                    workingsheet.write(row, 2, match.group(2))
                    workingsheet.write(row, 3, match.group(3))
                    workingsheet.write(row, 4, match.group(4))
                    workingsheet.write(row, 5, match.group(5))
                    row += 1
                else:
                    match = re.search(r'#\s(V\d+):(.*)', line)
                    if match:
                        workingsheet.write(row, 1, match.group(1))
                        workingsheet.write(row, 3, match.group(2))
                        row += 1

        elif match and match.group(1) == 'V8':
            workingsheet = workbook.get_worksheet_by_name(i18n.t('Anti-RE - Android'))
            row = 3
            with open(join(mypath, filename)) as file:
                datafile = file.readlines()

            for line in datafile:
                match = re.search(r'\|\s\*\*(\d\.\d+)\*\*\s\|\s(\w+‑\w+‑\d+)\s\|\s(.*)\s\|\s(✓)\s\|', line)
                if match:
                    workingsheet.write(row, 1, match.group(1))
                    workingsheet.write(row, 2, match.group(2))
                    workingsheet.write(row, 3, match.group(3))
                    workingsheet.write(row, 4, match.group(4))
                    row += 1
                else:
                    match = re.search(r'###\s(.*)', line)
                    if match:
                        workingsheet.write(row, 3, match.group(1))
                        row += 1

    workbook.close()
