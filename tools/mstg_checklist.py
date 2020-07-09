import i18n
import xlsxwriter
from os import listdir, mkdir
from os.path import isfile, join
import re


def createchecklist(masvs, lang):
    i18n.load_path.append('translations/')
    i18n.set('filename_format', 'checklist-{locale}.json')
    i18n.set('locale', lang)

    if lang == "en":
        mypath = '../Document'
    else:
        mypath = '../Document-' + lang

    try:
        mkdir("../Generated")
    except OSError:
        print("Directory ../Generated already created")

    workbook = xlsxwriter.Workbook('../Generated/Mobile_App_Security_Checklist-' + lang + '.xlsx')

    # Worksheet 'Dashboard'
    workingsheet = workbook.add_worksheet(i18n.t('Dashboard.worksheet'))
    workingsheet.set_column(0, 0, 1.5)
    workingsheet.set_column(1, 1, 8)
    workingsheet.set_column(2, 2, 16.33)
    workingsheet.set_column(3, 3, 91.67)

    title_format = workbook.add_format()
    title_format.set_font_name('Trebuchet MS')
    title_format.set_font_size(14)
    title_format.set_align('top')
    title_format.set_bold()
    title_format.set_bg_color('#EBEBEB')
    title_format.set_border()
    title_format.set_text_wrap()

    workingsheet.merge_range(1, 1, 6, 3, i18n.t('Dashboard.title'), title_format)

    table_title_format = workbook.add_format()
    table_title_format.set_bold()
    table_title_format.set_bg_color('#969696')
    table_title_format.set_border()
    table_title_format.set_font_name('Trebuchet MS')
    table_title_format.set_font_size(10)
    table_title_format.set_align('vcenter')
    table_row_title = workbook.add_format()
    table_row_title.set_bold()
    table_row_title.set_border()
    table_row_title.set_font_name('Trebuchet MS')
    table_row_title.set_font_size(10)
    table_row_title.set_align('vcenter')
    table_row_title.set_text_wrap()
    table_row_content = workbook.add_format()
    table_row_content.set_bold()
    table_row_content.set_border()
    table_row_content.set_font_name('Trebuchet MS')
    table_row_content.set_font_size(10)
    table_row_content.set_align('vcenter')

    # General Testing Information
    workingsheet.merge_range(9, 1, 9, 3, i18n.t('Dashboard.table_info.title'), table_title_format)
    workingsheet.merge_range(10, 1, 10, 2, i18n.t('Dashboard.table_info.MASVS_version'), table_row_title)
    workingsheet.merge_range(11, 1, 11, 2, i18n.t('Dashboard.table_info.link_MASVS'), table_row_title)
    workingsheet.merge_range(12, 1, 12, 2, i18n.t('Dashboard.table_info.MSTG_version'), table_row_title)
    workingsheet.merge_range(13, 1, 13, 2, i18n.t('Dashboard.table_info.link_MSTG'), table_row_title)
    workingsheet.set_row(14, 40)
    workingsheet.merge_range(14, 1, 14, 3, i18n.t('Dashboard.table_info.explanation'), table_row_title)
    workingsheet.merge_range(15, 1, 15, 2, i18n.t('Dashboard.table_info.Client_Name:'), table_row_title)
    workingsheet.merge_range(16, 1, 16, 2, i18n.t('Dashboard.table_info.Test-Location:'), table_row_title)
    workingsheet.merge_range(17, 1, 17, 2, i18n.t('Dashboard.table_info.Start_Date:'), table_row_title)
    workingsheet.merge_range(18, 1, 18, 2, i18n.t('Dashboard.table_info.Closing_Date:'), table_row_title)
    workingsheet.merge_range(19, 1, 19, 2, i18n.t('Dashboard.table_info.Name_Tester:'), table_row_title)
    workingsheet.merge_range(20, 1, 20, 2, i18n.t('Dashboard.table_info.Testing_Scope'), table_row_title)
    workingsheet.merge_range(21, 1, 21, 2, i18n.t('Dashboard.table_info.Verification_Level'), table_row_title)

    # Testing information Android
    workingsheet.merge_range(23, 1, 23, 3, i18n.t('Dashboard.table_Android.title'), table_title_format)

    # Testing information iOS
    workingsheet.merge_range(30, 1, 30, 3, i18n.t('Dashboard.table_iOS.title'), table_title_format)

    # Client Representatives and Contact Information
    skyblue_format = workbook.add_format()
    skyblue_format.set_bg_color('#AFD7FF')
    skyblue_format.set_border()
    workingsheet.merge_range(37, 1, 37, 3, i18n.t('Dashboard.table_contacts.title'), table_title_format)

    workingsheet.merge_range(38, 1, 38, 3, '', skyblue_format)

    workingsheet.merge_range(44, 1, 44, 3, '', skyblue_format)


    # Worksheet Management Summary
    workingsheet = workbook.add_worksheet(i18n.t('ManagementSummary.worksheet'))

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
