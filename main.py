from booking.booking import Booking
from time import sleep
from booking.journey_detail import Detail

# Taking detail of the journey like source, destination, journey_date
source = Detail.source_detail()
destination = Detail.destination_detail()
j_date = Detail.journey_date()

with Booking() as bot:
    bot.implicitly_wait(30)
    bot.land_first_page()
    bot.maximize_window()
    bot.sel_source(source)
    bot.sel_destination(destination)
    bot.journey_date(j_date)
    bot.search_btn()

    sleep(5)
