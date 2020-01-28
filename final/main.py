from cycle import prepare_cycle_data
from service_meter_reading import prepare_service_meter_reading_data

def run():
    prepare_cycle_data()
    prepare_service_meter_reading_data()


if __name__ == '__main__':
    run()
