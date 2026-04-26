class Address:
    """A class representing a physical address"""

    def __init__(self,street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

        

    def format_address(self):
        """Return formatted address String."""
        return f'Street : {self.street} \nCity : {self.city} \nState : {self.state} \nZip Code : {self.zip_code}'