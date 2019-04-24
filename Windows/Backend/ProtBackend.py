import os.path
os.chdir(r'C:\\Harddrive_Desktop\\Python\\TECAN_Worklist\\Microsoft\\Backend')

import xlrd
import csv 
import pandas as pd
import WorklistFrontend

global dilution
global final_vol


csv_direct = r'C:\\Harddrive_Desktop\\Python\\TECAN_Worklist\\Microsoft\\Lunatic csv file'
txt_direct = r'C:\\Harddrive_Desktop\\Python\\TECAN_Worklist\\Microsoft\\TECAN gwl file'
xlsx_direct = r'C:\\Harddrive_Desktop\\Python\\TECAN_Worklist\\Microsoft\\Lunatic xlsx file'
os.chdir(xlsx_direct)

dict_cd = {'A1': 1, 'B1': 2,'C1': 3,'D1': 4,'E1': 5,'F1': 6,'G1': 7,'H1': 8,'A2': 9,'B2': 10,'C2': 11,'D2': 12,'E2': 13,'F2': 14,
    'G2': 15,'H2': 16,'A3': 17,'B3': 18,'C3': 19,'D3': 20,'E3': 21,'F3': 22,'G3': 23,'H3': 24,'A4': 25,'B4': 26,'C4': 27,'D4': 28,
    'E4': 29,'F4': 30,'G4': 31,'H4': 32,'A5': 33,'B5': 34,'C5': 35,'D5': 36,'E5': 37,'F5': 38,'G5': 39,'H5': 40,'A6': 41,'B6': 42,
    'C6': 43,'D6': 44,'E6': 45,'F6': 46,'G6': 47,'H6': 48,'A7': 49,'B7': 50,'C7': 51,'D7': 52,'E7': 53,'F7': 54,'G7': 55,'H7': 56,
    'A8': 57,'B8': 58,'C8': 59,'D8': 60,'E8': 61,'F8': 62,'G8': 63,'H8': 64,'A9': 65,'B9': 66,'C9': 67,'D9': 68,'E9': 69,'F9': 70,
    'G9': 71,'H9': 72,'A10': 73,'B10': 74,'C10': 75,'D10': 76,'E10': 77,'F10': 78,'G10': 79,'H10': 80,'A11': 81,'B11': 82,'C11': 83,
    'D11': 84,'E11': 85,'F11': 86,'G11': 87,'H11': 88,'A12': 89,'B12': 90,'C12': 91,'D12': 92,'E12': 93,'F12': 94,'G12': 95,'H12': 96}

dict_dc = {1: 'A1', 2: 'B1', 3: 'C1', 4: 'D1', 5: 'E1', 6: 'F1', 7: 'G1', 8: 'H1', 9: 'A2', 10: 'B2', 11: 'C2', 12: 'D2', 13: 'E2', 14: 'F2',
    15: 'G2', 16: 'H2', 17: 'A3', 18: 'B3', 19: 'C3', 20: 'D3', 21: 'E3', 22: 'F3', 23: 'G3', 24: 'H3', 25: 'A4', 26: 'B4', 27: 'C4', 28: 'D4', 29: 'E4',
    30: 'F4', 31: 'G4', 32: 'H4', 33: 'A5', 34: 'B5', 35: 'C5', 36: 'D5', 37: 'E5', 38: 'F5', 39: 'G5', 40: 'H5', 41: 'A6', 42: 'B6', 43: 'C6', 44: 'D6',
    45: 'E6', 46: 'F6', 47: 'G6', 48: 'H6', 49: 'A7', 50: 'B7', 51: 'C7', 52: 'D7', 53: 'E7', 54: 'F7', 55: 'G7', 56: 'H7', 57: 'A8', 58: 'B8', 59: 'C8',
    60: 'D8', 61: 'E8', 62: 'F8', 63: 'G8', 64: 'H8', 65: 'A9', 66: 'B9', 67: 'C9', 68: 'D9', 69: 'E9', 70: 'F9', 71: 'G9', 72: 'H9', 73: 'A10', 74: 'B10',
    75: 'C10', 76: 'D10', 77: 'E10', 78: 'F10', 79: 'G10', 80: 'H10', 81: 'A11', 82: 'B11', 83: 'C11', 84: 'D11', 85: 'E11', 86: 'F11', 87: 'G11', 88: 'H11', 89: 'A12',
    90: 'B12', 91: 'C12', 92: 'D12', 93: 'E12', 94: 'F12', 95: 'G12', 96: 'H12'}


def csv_from_excel(filename):
    #absolute path when opening the filehandle for writing.
    csv_file = os.path.join(csv_direct, str(filename[:-5]) + '.csv')
    try:
        wb = xlrd.open_workbook(filename)
        #find excel sheet of interest
        sh = wb.sheet_by_name('Report')
        #open for writing ('w') and for generating new files ('+')
        your_csv_file = open(csv_file, 'w+')
        #set csv writer and write rows
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        your_csv_file.close()
        wb.release_resources()
        del wb
    except xlrd.biffh.XLRDError:
        wb.release_resources()
        del wb
        print("Oops, file: " + str(filename) + " is an invalid file.")


def worklist_gen(df):
    global dilution
    global final_vol
    global volume_dil
    df_mod = df
    dilution = float(dilution)
    final_vol = float(final_vol)
    #pandas
    lunatic = pd.read_csv(df_mod, sep = ',')
    #change name of column to row of selection (in which case is 1)
    lunatic.columns = lunatic.iloc[15]
    #remove columns using range 
    lunatic = lunatic.drop(lunatic.index[range(0,16)])

    prot_str = ""
    dil_str = ""
    na_list = list()
    belowconc_list = list()
    below20_list = list()
    out_range = list()
    out_range_dest = list()
    dest_diff_list = list()
    sample_num_loc = dict_cd[sample_loc[:1].upper() + sample_loc[1:]]
    position = sample_num_loc
    dest_num_loc = dict_cd[dest_loc[:1].upper() + dest_loc[1:]]
    dest_position = dest_num_loc
    #define position dil
    if 'trough' in dil_type_source.lower():
        position_dil = 1
    else:
        position_dil = position
    
    for index, row in lunatic.iterrows():
        while position < 97 and dest_position < 97:
            if 'trough' in dil_type_source.lower():
                if position_dil > 8:
                    position_dil = 1
            if type(row['A280 Concentration\n(mg/ml)']) == float:
                na_list.append(row['Plate\nPosition'])
                break
            elif (float(row['A280 Concentration\n(mg/ml)']) / dilution) < 0.8:
                belowconc_list.append(row['Plate\nPosition'])
                break
            else:
                row_val = float(row['A280 Concentration\n(mg/ml)'])
                if (dilution/row_val) < 0.2:
                    below20_list.append(row['Plate\nPosition'])
                volume_prot = 1.0 * ((final_vol * dilution) / row_val)
                volume_dil = final_vol - volume_prot
                if volume_prot > final_vol:
                    volume_prot = final_vol
                    volume_dil = 0
                
                prot_str += (1*(f"A;{rack_source};;{rack_type_source};{str(position)};;{str('%.2f' % (volume_prot))};;;\n" + 
                            f"D;{rack_dest};;{rack_type_dest};{str(dest_position)};;{str('%.2f' % (volume_prot))};;;\n") +
                            "W;\n")
                dil_str += (1*(f"A;{dil_source};;{dil_type_source};{str(position_dil)};;{str('%.2f' % volume_dil)};;;\n" +  
                            f"D;{rack_dest};;{rack_type_dest};{str(dest_position)};;{str('%.2f' % volume_dil)};;;\n") +
                            "W;\n")      

                break
        else:        
            if position > 96:
                out_range += ([row['Plate\nPosition']])
            elif dest_position > 96:
                dest_diff_list.append(dest_position - 97)
            else:
                pass
        position += 1
        dest_position += 1
        position_dil += 1

    #track which source samples will not be included in destination plate due to exceeding plate range
    if len(dest_diff_list) != 0:
        for i in dest_diff_list:
            out_range_dest += [dict_dc[(96 - i)]]

    na_str = ', '.join([i 
        for i in na_list 
        if na_list[0] != ''])
    belowconc_str = ', '.join([i
        for i in belowconc_list
        if belowconc_list[0] != ''])
    caut_str = ', '.join([i 
        for i in below20_list
        if below20_list[0] != ''])
    out_range_str = ', '.join([i 
        for i in out_range 
        if out_range[0] != ''])
    out_range_dest_str = ', '.join([i 
        for i in out_range_dest[::-1] 
        if out_range_dest[0] != ''])

    warning_str = "" 
    range_str = ""
    if len(belowconc_str) + len(na_str) != 0:
        warning_str += (20*"-") + "THE FOLLOWING WELLS WILL NOT BE NORMALIZED." + (20*"-") + "\n"
        if len(na_str) != 0:
            warning_str += "NA VALUES: \n" + na_str + "\n\n"
        if len(belowconc_str) != 0:
            warning_str += "SAMPLE CONC. < 80% FINAL CONC.: \n" + belowconc_str + "\n\n"
    if len(caut_str) != 0:
        warning_str += (10*"-") + "THE FOLLOWING WELLS WILL BE NORMALIZED - PROCEED WITH CAUTION." + (10*"-") + "\n" 
        if len(caut_str) != 0:
            warning_str += "ASP. VOL. < 20% FINAL VOL.: \n" + caut_str
    if len(out_range_str) + len(out_range_dest_str) != 0:
        range_str += (10*"-") + "THE FOLLOWING WELLS WILL NOT BE NORMALIZED - OUT OF PLATE RANGE." + (10*"-") + "\n"
        if len(out_range_str) != 0:
            range_str += "THE FOLLOWING SAMPLE(S) MEASURED ON LUNATIC NOT INCLUDED IN WORKLIST: \n" + out_range_str + "\n\n"
        if len(out_range_dest_str) != 0:
            range_str += "THE FOLLOWING SAMPLE(S) IN SOURCE PLATE NOT INCLUDED IN DESTINATION PLATE: \n" + out_range_dest_str + "\n\n"

    return(prot_str, dil_str, warning_str, range_str)


for filename in os.listdir(os.getcwd()):
    if filename[-5:] == '.xlsx':
        try:
            csv_from_excel(filename)
            csv_file = os.path.join(csv_direct, str(filename[:-5]) + '.csv')
            prot, dil ,warn, out = worklist_gen(csv_file)
        except KeyError:
            continue
        
        new_direct = txt_direct + "/" + str(filename[:-5])
        #if the directory path you want to make is not there, make it. 
        #don't override existing directory
        if not os.path.exists(new_direct):
                os.makedirs(new_direct)
        else: 
            continue

        #write prot and dil volume and store them in the newly created directory
        if prot != "":
            prot_txt = os.path.join(new_direct, 'PROT_TECAN.gwl')
            prot_file= open(prot_txt, "w+")
            prot_file.write(prot)
            prot_file.close()
        if dil != "":
            dil_txt = os.path.join(new_direct, 'DIL_TECAN.gwl')
            dil_file = open(dil_txt, "w+")
            dil_file.write(dil)
            dil_file.close()
        if warn != "":
            #adds warning .txt file for ommitted and advisory protein samples (in plate coord.)
            caut_txt = os.path.join(new_direct, 'WARNING.txt')
            caut_file = open(caut_txt, "w+")
            caut_file.write(warn)
            caut_file.close()
        if out != "":
            #adds .txt file for samples that exceeded destination plate range from Lunatic plate.
            out_txt = os.path.join(new_direct, 'RANGE_FAIL.txt')
            out_file = open(out_txt, "w+")
            out_file.write(out)
            out_file.close()

    else:
        continue
