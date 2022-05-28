import calendar
from datetime import *
from time import strftime
import calendar
from flaskflights.models import AvailableFlights, Aircraft


def addToCalender():
    syberJet1 = Aircraft(name='SyberJet 1', model='SJ30i', capacity=6)
    syberJet2 = Aircraft(name='SyberJet 2', model='SJ30i', capacity=6)
    cirrus1 = Aircraft(name='Cirrus 1', model='SF50', capacity=4)
    cirrus2 = Aircraft(name='Cirrus 2', model='SF50', capacity=4)
    hondaJet1 = Aircraft(name='HondaJet 1', model='Elite', capacity=5)
    hondaJet2 = Aircraft(name='HondaJet 2', model='Elite', capacity=5)

    for monthNum in range(6, 10):
        month = calendar.monthcalendar(2022, monthNum)
        week = [week for week in month]
        # from dairy flat
        for i in range(5):
            dateFlight = week[i][4] # day of week
            if dateFlight:
                dairyToRotoSyd = AvailableFlights(timeOfFlight="8:00 A.M.", dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=4,flyingFrom='Dairy Flat',stopsAt='Rotorua', flyingTo='Sydney',aircraft=syberJet1,seatsLeft=syberJet1.capacity)
            dateFlight = week[i][0]
            for day in range(5):
                if dateFlight:
                    toRotoM = AvailableFlights(timeOfFlight="8:00 A.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=day,flyingFrom='Dairy Flat',stopsAt=None,flyingTo='Rotorua',aircraft=cirrus1,seatsLeft=cirrus1.capacity)
                    toRotoA = AvailableFlights(timeOfFlight="6:00 P.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=day,flyingFrom='Dairy Flat',stopsAt=None,flyingTo='Rotorua',aircraft=cirrus2,seatsLeft=cirrus2.capacity)
            dateFlight = week[i][1]
            if dateFlight:
                toTuutaT = AvailableFlights(timeOfFlight="1:00 P.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=1,flyingFrom='Dairy Flat',stopsAt=None,flyingTo='Tuuta', aircraft=hondaJet1,seatsLeft=hondaJet1.capacity)
            dateFlight = week[i][5]
            if dateFlight:
                toTuutaF = AvailableFlights(timeOfFlight="1:00 P.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=4,flyingFrom='Dairy Flat',stopsAt=None,flyingTo='Tuuta',aircraft=hondaJet1, seatsLeft=hondaJet1.capacity)
            dateFlight = week[i][0]
            if dateFlight:
                toTekapo = AvailableFlights(timeOfFlight="3:00 P.M.", dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=0,flyingFrom='Dairy Flat',stopsAt=None,flyingTo='Tekapo',aircraft=hondaJet2,seatsLeft=hondaJet2.capacity)
            for days in range(0, 6, 2):
                dateFlight = week[i][days]
                if dateFlight:
                    toGBI = AvailableFlights(timeOfFlight="9:00 A.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=days,flyingFrom='Dairy Flat', stopsAt=None,flyingTo='Great Barrier Island',aircraft=cirrus1,seatsLeft=cirrus1.capacity)
            dateFlight = week[i][5]
            if dateFlight:
                rotoToSyd = AvailableFlights(timeOfFlight="9:00 A.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=4,flyingFrom='Rotorua', stopsAt=None,flyingTo='Sydney',aircraft=syberJet1,seatsLeft=syberJet1.capacity)
            for day in range(5):
                dateFlight= week[i][day]
                rotoToDairyN = AvailableFlights(timeOfFlight="12:00 P.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=day,flyingFrom='Rotorua', stopsAt=None,flyingTo='Dairy Flat',aircraft=cirrus2,seatsLeft=cirrus2.capacity)
                rotoToDairyE = AvailableFlights(timeOfFlight="5:00 P.M.",dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),dayOfFlight=day,flyingFrom='Rotorua', stopsAt=None,flyingTo='Dairy Flat',aircraft=cirrus2,seatsLeft=cirrus2.capacity)
            #from tuuta
            # wednesday and saturday - to dairy flat - HondaJets
            dateFlight = week[i][3]
            if dateFlight:
                tuutaToDFw = AvailableFlights(timeOfFlight="5:00 P.M.",
                                                dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),
                                                dayOfFlight=2, flyingFrom='Tuuta', stopsAt=None, flyingTo='Dairy Flat',
                                                aircraft=hondaJet2, seatsLeft=hondaJet2.capacity)
            dateFlight = week[i][6]
            if dateFlight:
                tuutaToDFs = AvailableFlights(timeOfFlight="5:00 P.M.",
                                              dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),
                                              dayOfFlight=5, flyingFrom='Tuuta', stopsAt=None, flyingTo='Dairy Flat',
                                              aircraft=hondaJet2, seatsLeft=hondaJet2.capacity)
            # from sydney
            # sunday afternoon - to dairy flat - syberjet
            dateFlight = week[i][-1]
            if dateFlight:
                sydToDF = AvailableFlights(timeOfFlight="5:00 P.M.",
                                              dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),
                                              dayOfFlight=6, flyingFrom='Sydney', stopsAt=None, flyingTo='Dairy Flat',
                                              aircraft=syberJet2, seatsLeft=syberJet2.capacity)
            #from tekapo
            # friday - to dairy flat - hondajet
            dateFlight = week[i][5]
            if dateFlight:
                tekaToDF = AvailableFlights(timeOfFlight="1:00 P.M.",
                                              dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),
                                              dayOfFlight=4, flyingFrom='Tekapo', stopsAt=None, flyingTo='Dairy Flat',
                                              aircraft=hondaJet1, seatsLeft=hondaJet1.capacity)
            # from great barrier island
            # monday, friday, saturday - to dairy flat - cirrus jets
            dateFlight = week[i][5]
            if dateFlight:
                tekaToDF = AvailableFlights(timeOfFlight="1:00 P.M.",
                                              dateOfFlight=strftime("%{}/%{}/%2022".format(dateFlight, monthNum)),
                                              dayOfFlight=4, flyingFrom='Tekapo', stopsAt=None, flyingTo='Dairy Flat',
                                              aircraft=hondaJet1, seatsLeft=hondaJet1.capacity)

addToCalender()
