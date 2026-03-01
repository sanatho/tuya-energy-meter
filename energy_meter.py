class EnegeryMeter:
    def __init__(self, data):
        """
        Constructor of energy meter
        :param data: raw data from tinytuya 
        """
        
        self.voltage = float(data['107'])/10
        self.current = float(data['106'])/1000
        self.power = float(data['105'])/10

    def __str__(self):
        return f'{{\'status\': \'up\', \'voltage\':{self.voltage}, \'current\':{self.current}, \'power\':{self.power}}}'
        