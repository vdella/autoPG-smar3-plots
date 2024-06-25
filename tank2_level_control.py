import matplotlib.pyplot as plt
from __init__ import standard_level_file_data, standard_sp_file_data, standard_valve_file_data
from graphic import join_graphic_info_from


if __name__ == '__main__':
    level_info = join_graphic_info_from(standard_level_file_data)
    sp_info = join_graphic_info_from(standard_sp_file_data)
    valve_info = join_graphic_info_from(standard_valve_file_data)

    plt.plot(level_info.time,
             level_info.result,
             label='Level',
             color='green',
             linestyle='solid')
    plt.plot(sp_info.time,
             sp_info.result,
             label='Setpoint',
             color='blue',
             linestyle='dotted')
    plt.plot(valve_info.time,
             valve_info.result,
             label='Valve',
             color='red',
             linestyle='dashed')

    plt.legend()

    plt.savefig('graphics/level-sp-valve.png')
    plt.show()
