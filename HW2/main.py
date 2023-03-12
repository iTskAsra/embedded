class ChillerSuperState:
    def __init__(self, states) -> None:
        self.isOn = False
        self.speed = 'Off'
        self.states = states
        self.active_state_index = 0



class HeaterSuperState:
    def __init__(self, states) -> None:
        self.isOn = False
        self.speed = 'Off'
        self.states = states
        self.active_state_index = 0

class State:
    def __init__(self, name, transitions, unit) -> None:
        self.name = name
        self.unit = unit
        self.transitions = transitions

    
    def __str__(self) -> str:
        return f'Active unit is the {self.unit} and possible transitions are {self.transitions}'
        


init_temp = int(input("Initial room temperature:"))
chiller_states = []
heater_states = []
chiller_states.append(State('Low', ['1. <20', '2. >25'], 'Chiller'))
chiller_states.append(State('Mid', ['1. <25', '2. >30'], 'Chiller'))
chiller_states.append(State('High', ['1. <30'], 'Chiller'))
heater_states.append(State('Low', ['1. >20', '2. <15'], 'Heater'))
heater_states.append(State('Mid', ['1. <10', '2. >15'], 'Heater'))
heater_states.append(State('High', ['1. >10'], 'Heater'))

hss = HeaterSuperState(heater_states)
css = ChillerSuperState(chiller_states)
current_unit = 'chiller'
if init_temp > 30:
    css.isOn = True
    css.active_state_index = 2
elif init_temp > 25:
    css.isOn = True
    css.active_state_index = 1
elif init_temp > 20:
    css.isOn = True
elif init_temp > 15:
    hss.isOn = True
    current_unit = 'heater'
elif init_temp > 10:
    hss.isOn = True
    current_unit = 'heater'
    hss.active_state_index = 1
else:
    hss.isOn = True
    current_unit = 'heater'
    hss.active_state_index = 2

chiller = False
if current_unit == 'chiller':
    chiller = True
while True:
    if current_unit == 'chiller':
        print(css.states[css.active_state_index])
    else:
        print(hss.states[hss.active_state_index])
    
    inp = int(input('Your choice of transition:'))
    if chiller:
        if css.active_state_index == 0:
            if inp == 1:
                chiller = False
                css.isOn = False
                hss.isOn = True
                current_unit = 'heater'
                hss.active_state_index = 0
            else:
                css.active_state_index = 1
        elif css.active_state_index == 1:
            if inp == 1:
                css.active_state_index = 0
            else:
                css.active_state_index = 2
        else:
            css.active_state_index = 1
    else:
        if hss.active_state_index == 0:
            if inp == 1:
                chiller = True
                hss.isOn = False
                css.isOn = True
                current_unit = 'chiller'
                css.active_state_index = 0
            else:
                hss.active_state_index = 1
        elif hss.active_state_index == 1:
            if inp == 1:
                hss.active_state_index = 2
            else:
                hss.active_state_index = 0
        else:
            hss.active_state_index = 1