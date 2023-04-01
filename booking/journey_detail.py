class Detail:
    def __init__(self):
        pass

    @staticmethod
    def source_detail():
        source = input("Enter source of the train (CNB): ")
        return source

    @staticmethod
    def destination_detail():
        destination = input("Enter destination of the train (BBS): ")
        return destination

    @staticmethod
    def journey_date():
        j_date = input("Enter journey date (in DD/MM/YYYY format): ")
        return j_date
