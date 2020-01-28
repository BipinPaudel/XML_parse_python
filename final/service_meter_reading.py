from prepare_csv import prepare_csv
import xml.etree.ElementTree as ET


def prepare_service_meter_reading_data():
    print("preparing service_meter_reading data")
    columns = ['rid', 'servicemeterreading_oid', 'smu', 'readingdate_utc', 'machine']
    data = []
    tree_2 = ET.parse("test_xml.xml")
    root = tree_2.getroot()
    for node in root.iter('servicemeterreadings'):
        for cycle in node.iter('servicemeterreading'):
            single_list = [cycle.attrib['rid']]
            for oid in cycle.findall("servicemeterreading_oid"):
                single_list.append(oid.text)
            for ecf_class_id in cycle.findall("smu"):
                single_list.append(ecf_class_id.text)
            for start_time_utc in cycle.findall("readingdate_utc"):
                single_list.append(start_time_utc.text)
            for end_time_utc in cycle.findall("machine"):
                single_list.append(end_time_utc.text)
            data.append(single_list)
    prepare_csv("service_meter_reading.csv", columns, data)
    print(len(data))




