import csv
import re
from home_work_decorator__task_2 import logger

with open("folder/phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


@logger("folder/info_re.log")
def select_number_phone(contacts_list):
    pattern_number_phone = r'(\+7|8)(\s*)' \
                 r'(\(*)(\d{3})(\)*)(\s*)' \
                 r'(\-*)(\d{3})(\s*)(\-*)' \
                 r'(\d{2})(\s*)(\-*)' \
                 r'(\d{2})(\s*)' \
                 r'(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    repl_new_number_phone = r"+7(\4)\8-\11-\14\15\17\18\20"
    _update_contact_list = []
    for element in contacts_list:
        contact_string = ",".join(element)
        format_contact_string = re.sub(pattern_number_phone, repl_new_number_phone, contact_string)
        _update_contact_list.append(format_contact_string.split(','))
    return _update_contact_list


@logger("folder/info_re.log")
def select_full_name():
    _update_1_contact_list = []
    pattern_name = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)'
    repl_new_name = r'\1,\4,\7,\11,'
    for element in update_contact_list:
        my_string = ",".join(element)
        format_contact_string = re.sub(pattern_name, repl_new_name, my_string)
        _update_1_contact_list.append(format_contact_string.split(','))
    return _update_1_contact_list


@logger("folder/info_re.log")
def deleting_a_duplicate():
    my_list = []
    _my_dict_1 = {}
    my_dict_1 = {}
    _my_dict = {}
    my_dict = {}
    # уберем диблирующие запятые
    pattern_name = r'\,{1,}'
    repl_new_name = r','
    for elem in update_1_contact_list:
        my_string = ",".join(elem)
        format_contact_string = re.sub(pattern_name, repl_new_name, my_string)
        my_list.append(format_contact_string.split(','))
    #for elem in my_list:
        #print(elem)

    # заполним словарь из повторяющихся имен
    for i in range(0, len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if my_list[i][0] == my_list[j][0]:
                #print(f"{my_list[i][0]}  и  {my_list[j][0]}")
                _list = []
                for a in my_list[i][2:]:
                    if a in _list:
                        continue
                    else:
                        _list.append(a)
                for b in my_list[j][2:]:
                    if b in _list:
                        continue
                    else:
                        _list.append(b)
                _my_dict_1 = {(my_list[i][0], my_list[i][1]): _list}
            my_dict_1.update(_my_dict_1)
    #for el in my_dict_1.keys():
        #print(el)

    # заполним словарь из неповторяющихся имен
    for elem in my_list:
        for _key in my_dict_1.keys():
            if elem[0] not in _key:
                _my_dict = {(elem[0], elem[1]): elem[2:]}
            my_dict.update(_my_dict)

    # итоговый словарь - без дублирующих записей
    my_dict.update(my_dict_1)
    #for el in my_dict.items():
        #print(el)

    # промежуточный список
    _list_phonebook = []

    for _keys, _values in my_dict.items():
        line_list = (', '.join(_keys)) + ", " + (', '.join(_values).replace(', ,', ','))
        _list_phonebook.append(line_list)

    # итоговый список для записи в csv
    new_list_phonebook = []

    for elem in _list_phonebook:
        new_list_phonebook.append(elem.split(','))
    return new_list_phonebook


@logger("folder/info_re.log")
def writer_csv_file(write_list):
    with open("folder/new_phonebook.csv", "w",  encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(write_list)

if __name__ == "__main__":
    update_contact_list = select_number_phone(contacts_list)
    update_1_contact_list = select_full_name()
    write_list = deleting_a_duplicate()
    select_number_phone(contacts_list)
    select_full_name()
    print(deleting_a_duplicate())
    writer_csv_file(write_list)
