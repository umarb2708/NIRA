def get_battery_status(bat_module,obj1):
    if(obj1.initialized==0):
        ina=bat_module(shunt_ohms=0.1,
             max_expected_amps = 0.6,
             address=0x40)
        ina.configure(voltage_range=ina.RANGE_16V,
              gain=ina.GAIN_AUTO,
              bus_adc=ina.ADC_128SAMP,
              shunt_adc=ina.ADC_128SAMP)
        obj1.initialized=1
    obj1.v=ina.voltage()
    obj1.i= ina.current()
    obj1.p=ina.power()

