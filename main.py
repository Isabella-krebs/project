

    ## Bobcat E35 Calculator 

    
import math

#Standard Known Values and Conversions 
Y = 62.4       # Density of Water

#Code
def custom_equation_calculator():
    print("=== Bobcat E35 Calculator ===")
    
    variable_map = {
        'Wload': 'load Weight (lb)',
        'Wop' : 'Assumed Total Operating weight (lb)',
        'xpta' : 'Distance of COG Track A x (ft)',
        'ypta' : 'Distance of COG Track A y (ft)' ,
        'xptb' : 'Distance of COG Track B x (ft)',
        'yptb' : 'Distance of COG Track B y (ft)',
        'xls' : 'Distance of COG Lower Structure x (ft)',
        'yls' : 'Distance of COG Lower Structure y (ft)',
        'zls' : 'Distance of COG Lower Structure z (ft)',
        'xus' : 'Distance of COG Upper Structure x (ft)',
        'yus' : 'Distance of COG Upper Structure y (ft)',
        'zus' : 'Distance of COG Upper Structure z (ft)',
        'xcw' : 'Distance of COG Counter Weight x (ft)',
        'ycw' : 'Distance of COG Counter Weight y (ft)',
        'zcw' : 'Distance of COG Counter Weight z (ft)',
        'xarm' : 'Distance of COG Arm and Boom x (ft)',
        'yarm' : 'Distance of COG Arm and Boom y (ft)',
        'zarm' : 'Distance of COG Arm and Boom z (ft)',
        'xbl' : 'Distance of COG Load  & Bucket x (ft)',
        'ybl' : 'Distance of COG Load & Bucket y (ft)',
        'zbl' : 'Distance of COG Load & Bucket z (ft)',
        'ptw' : 'Track Width (ft)',
        'ptl' : 'Track Length (ft)',
        'rl' : 'Rake length (ft)',
        'pts' : 'Distance Between Two Tracks (center to center) (ft)',
        'l' : 'Length (in)',
        'w' : 'Width (in)',
        'h' : 'Height (in)',
        'hopc' : 'Height with Operator Cab (in)',
        'opw' : 'Operating Weight (lb)',
        'gp' : 'Ground Pressure (psi)',
        'ba' : 'Boom, Arm (lb)',
        'b' : 'Bucket (lb)',
        'tw' : 'Truck Weight (lb)',
        'cw' : 'Cab Weight (lb)',
        'COGc' : 'Center of gravity Cab (in)',
        'COGboom' : 'Center of gravity boom (in)',
        'COGbucket' : 'Center of gravity bucket (in)',
        'COGa' : 'Center of gravity arm (in)',
        'ftv' : 'Fuel Tank Volume (gal)',
        'mrgl' : 'Max Reach at Ground level (in)',
        'tsh' : 'Travel Speed - High (mph)',
        'tsl' : 'Travel Speed - Low (mph)',
        'adf' : 'Arm Digging Force (lbf)',
        'bdf' : 'Bucket Digging Force (lbf)',
        'lcb' : 'Rated Lift Capacity @ 10 ft over Blade (lb)',
        'lcs' : 'Rated Lift Capacity @ 10 ft over Side (lb)',
        'lr' : 'Lift Radius (in)',
        'bsl' : 'Boom Swing - left (degrees)',
        'bsr' : 'Boom Swing - Right (degrees)',
        'mdd' : 'Maximum Dig Depth (in)',
        'mdh' : 'Maximum Dump Height (in)',
        'mr' : 'Maximum reach (ft)',
        'fwf' : 'Fuel Weight Full (lb)',
        'Wpt' : 'Weight of Pontoon (lb)',
        'Wls' : 'Weight of lower structure (lb)',
        'Wu' : 'Weight of machine upper (lb)',
        'Wtop' : 'Weight of top (lb)',
        'Wft' : 'Estimated weight of fuel tank (tool box, and walkways) (lb)',
        'Wab' : 'Estimated Weight of boom, arm (lb)',
        'Wb' : 'Estimated Weight of the bucket (lb)',
        'Wbl' : 'Estimated weight of bucket and load (lb)',
        'Vp' : 'Volume of Single Pontoon (cf)',
        'lp' : 'Length of Single Pontoon (ft)',
        'bp' : 'Width of Single Pontoon (ft)',
        'hp' : 'Height of Single Pontoon (ft)',
        'Lbt' : 'Base Track Load (lb)',
        'NC' : 'Number of Components',
        'VC1' : 'Volume of Compartment 1',
        'VC2' : 'Volume of Compartment 2',
        'VC3' : 'Volume of Compartment 3',
        'MBFRPT' : 'Max buoyant force for right pontoon',
        'MBFLPT' : 'Max buoyant force for left pontoon',
        'OBFL' : 'Overturning buoyant force left',
        'OBFR' : 'Overturning buoyant force right',
        'UBL' : 'Utilization Buoyant Left',
        'UBR' : 'Utilization Buoyant Right',
        'cla' : 'Critical Lift Angle',
        'OMCA' : 'Overturing Moment at Critical Angle',
        'TDMCOGO' : 'Total Displacement of machine COG to overturn',
        'Wcw' : 'Weight of Counter Weight (lb)',
        'Θ' : 'Angle of Boom',
    }
    values = {}
    for short_var, description in variable_map.items():
        val = float(input(f"Enter {description}: "))
        values[short_var] = val
        
    try:
        ΣW = values['Wload'] + values['Wop']        # Sum of Machine Weights & load Weight
        Vu = ΣW / Y                                 # Volume of displaced water needed to float
        Vreq = Vu / 0.7                             # Total Volume with 30% above water
        Vp = Vreq / 2                               # Volume of each Pontoon
        bp = Vp / (values['lp'] * values['hp'])     # Width of Pontoon
        Fbr = Vp / Y                                # Max Bouyant force from right pontoon
        Lbt = ΣW / 2                                #Base Track Load
        Rad = values['Θ'] * 3.14/180                #Angle in Radians
        Cax = ((values['Wu'] * values['xus']) + (values['Wcw'] * values['xcw']) + (values['Wab'] * values['xarm']) + (values['Wbl'] * values['xbl'])) / values['Wtop'] #Lump center of gravity in x
        Cay = ((values['Wu'] * values['yus']) + (values['Wcw'] * values['ycw']) + (values['Wab'] * values['yarm']) + (values['Wbl'] * values['ybl'])) / values['Wtop'] #Lump center of gravity in y
        ΣMy = (Cax * values['Wtop']) + (values['Wpt'] * values['xpta']) + (values['Wpt'] * values['xptb']) + (values['Wls'] * values['xls'])                           # Y moment
        ΣMx = (Cay * values['Wtop']) + (values['Wpt'] * values['ypta']) + (values['Wpt'] * values['yptb']) + (values['Wls'] * values['yls'])                           # X moment
        Fdt = ΣMy / values['pts']                                                                                                                              # Force distribution in tracks
        Tad = Lbt + Fdt                                                                                                                                        # Track A Differential
        Tbd = Lbt - Fdt                                                                                                                                        # Track B Differential
        Dofb = ΣMx / ΣW                                                                                                                                        # Ecentricity Distance
        
        print(f"Sum of Machine Weights & load Weight : {ΣW}")
        print(f"Volume of displaced water needed to float : {Vu}")
        print(f"Total Volume with 30% above water : {Vreq}")
        print(f"Volume of each Pontoon : {Vp}")
        print(f"Width of Pontoon : {bp}")
        print(f"Max Bouyant force from right pontoon : {Fbr}")
        print(f"Base Track Load : {Lbt}")
        print(f"Angle in Radians : {Rad}")
        print(f"Lump center of gravity in x : {Cax}")
        print(f"Lump center of gravity in y : {Cay}")
        print(f"Y Moment : {ΣMy}")
        print(f"X moment : {ΣMx}")
        print(f"Force Distribution in Tracks : {Fdt}")
        print(f"Track A Differential : {Tad}")
        print(f"Track B Differential : {Tbd}")
        print(f"Ecentricity Distance : {Dofb}")
        
    except Exception as e:
        print("Calculation error :", e)

custom_equation_calculator()
