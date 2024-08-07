# HomeAssistant Dimplex Heatpump (modbus)
HomeAssistant Custom Component for reading data from Dimplex DHW300 Heatpump through ModbusTCP.
This requires the NWPM Touch extension installed on your Dimplex Heatpump

**IMPORTANT**  
unfortunately, this project is on hold - I consider to buy a dimplex heatpump, but I don't have one yet, so I can't really develop and test one.
A possible way to implement could be the following repository: [@chripuf/smarthomeNG-DimplexWP](https://github.com/chrpuf/smarthomeNG-DimplexWP)

**Modbus Datapoints taken from @chrpuf/smarthomeNG-DimplexWP:**
```
            "outdoor_temp" : {"type" : "register", "address" : 1, "count" : 1, "conVal" : 10},
            "return_temp" : {"type" : "register", "address" : 2, "count" : 1, "conVal" : 10},
            "set-point_return_temp" : {"type" : "register", "address" : 53, "count" : 1, "conVal" : 10},
            "hot_water_temp" : {"type" : "register", "address" : 3, "count" : 1, "conVal" : 10},
            "flow_temp" : {"type" : "register", "address" : 5, "count" : 1, "conVal" : 10},
            "heat_source_inlet_temp" : {"type" : "register", "address" : 6, "count" : 1, "conVal" : 10},
            "heat_source_outlet_temp" : {"type" : "register", "address" : 7, "count" : 1, "conVal" : 10},
            "hysteresis" : {"type" : "register", "address" : 47, "count" : 1, "conVal" : 10},
            "heating_rod" : {"type" : "register", "address" : 75, "count" : 1, "conVal" : 1},
            "heat_heating" : {"type" : "register", "address" : 5096, "count" : 3, "conVal" : 1},
            "heat_hot_water" : {"type" : "register", "address" : 5099, "count" : 3, "conVal" : 1},
            "operating_mode" : {"type" : "register", "address" : 5015, "count" : 1, "conVal" : 1},
            "hot_water_hysteresis" : {"type" : "register", "address" : 5045, "count" : 1, "conVal" : 1},
            "hot_water_set-point_temp" : {"type" : "register", "address" : 5047, "count" : 1, "conVal" : 1},
            "status_messages" : {"type" : "register", "address" : 103, "count" : 1, "conVal" : 1},
            "heat_pump_lock" : {"type" : "register", "address" : 104, "count" : 1, "conVal" : 1},
            "alerts" : {"type" : "register", "address" : 105, "count" : 1, "conVal" : 1},
            "sensors" : {"type" : "register", "address" : 106, "count" : 1, "conVal" : 1},
            "outlet_compressor" : {"type" : "coil", "address" : 41, "count" : 1},
            "outlet_primary_pump" : {"type" : "coil", "address" : 43, "count" : 1},
            "outlet_heating_rod" : {"type" : "coil", "address" : 44, "count" : 1},
            "outlet_heating_pump_M13" : {"type" : "coil", "address" : 45, "count" : 1},
            "outlet_hot_water_pump" : {"type" : "coil", "address" : 46, "count" : 1},
            "outlet_add_circ_pump" : {"type" : "coil", "address" : 49, "count" : 1},
            "outlet_heating_pump_M15" : {"type" : "coil", "address" : 51, "count" : 1},
            "outlet_heating_pump_M14" : {"type" : "coil", "address" : 59, "count" : 1},
            "outlet_heating_pump_M20" : {"type" : "coil", "address" : 61, "count" : 1}
```
