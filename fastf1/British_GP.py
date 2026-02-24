import fastf1

year = 2019
grand_prix = 10
session = 1

session = fastf1.get_session(year, grand_prix, session)
session.load()


driver_laps = session.laps.pick_drivers('HAM')  #drivers

lap = driver_laps.pick_fastest()

telemetry = lap.get_car_data()

print(telemetry.head())

