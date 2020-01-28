from prepare_csv import prepare_csv
import xml.etree.ElementTree as ET


def prepare_cycle_data():
    print("preparing cycle data")
    cycle_columns = ['rid', 'oid', 'ecf_class_id', 'starttime_utc', 'endtime_utc']
    data = []
    tree_2 = ET.parse("test_xml.xml")
    root = tree_2.getroot()
    for node in root.iter('cycles'):
        for cycle in node.iter('cycle'):
            single_list = [cycle.attrib['rid']]
            for oid in cycle.findall("cycle_oid"):
                single_list.append(oid.text)
            for ecf_class_id in cycle.findall("ecf_class_id"):
                single_list.append(ecf_class_id.text)
            for start_time_utc in cycle.findall("starttime_utc"):
                single_list.append(start_time_utc.text)
            for end_time_utc in cycle.findall("endtime_utc"):
                single_list.append(end_time_utc.text)
            data.append(single_list)
    prepare_csv("cycle.csv", cycle_columns, data)
    print(len(data))




