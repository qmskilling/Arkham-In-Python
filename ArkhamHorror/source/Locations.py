import sys

class Locations():
    def __init__(self):

        self.base_dict = {}
        self.base_dict['Downtown'] = ['Arkham Asylum','Bank of Arkham','Independence Square']
        self.base_dict['Uptown'] = ['St. Mary\'s Hospital','Ye Olde Magick Shoppe','Woods']
        self.base_dict['Miskatonic University'] = ['Administration Building','Library','Science Building']
        self.base_dict['Merchant District'] = ['River Docks','Unvisited Isle','The Unnamable']
        self.base_dict['Northside'] = ['Curiositie Shoppe','Newspaper','Train Station']
        self.base_dict['Easttown'] = ['Hibb\'s Roadhouse','Police Station','Jail Cell','Velma\'s Diner']
        self.base_dict['Southside'] = ['South Church','Historical Society','Ma\'s Boarding House']
        self.base_dict['French Hill'] = ['Silver Twilight Lodge','The Witch House']
        self.base_dict['Rivertown'] = ['General Store','Graveyard','Black Cave']
        self.base_dict['Other Worlds'] = ['Abyss','Another Dimension','City of the Great Race','Great Hall of Celeano','Plateau of Leng',\
            'R\'lyeh','The Dreamlands','Yuggoth']
        self.locations_base = sorted([value for key, value in self.base_dict.items() if key not in ['Other Worlds']])
        self.streets_base = sorted([key for key,value in self.base_dict.items() if key not in ['Other Worlds']])
        self.otherWorlds_base = sorted(self.base_dict['Other Worlds'])
        
        self.dunwich_dict = {}
        self.dunwich_dict['Backwoods Country'] = ['Cold Spring Glen','Whateley Farm','Wizard\'s Hill']
        self.dunwich_dict['Blasted Heath'] = ['Devil\'s Hopyard','Gardners\' Place','Harney Jones\' Shack']
        self.dunwich_dict['Village Commons'] = ['Bishop\'s Brook Bridge','Darke\'s Carnival','Dunwich Village']
        self.dunwich_dict['Other Worlds'] = ['Another Time','Lost Carcosa']
        self.locations_dunwich = sorted([value for key, value in self.dunwich_dict.items() if key not in ['Other Worlds']])
        self.streets_dunwich = sorted([key for key, value in self.dunwich_dict.items() if key not in ['Other Worlds']])
        self.streets_dunwich = self.streets_dunwich.append('Sentinel Hill')
        self.otherWorlds_dunwich = sorted(self.dunwich_dict['Other Worlds'])

        self.kingsport_dict = {}
        self.kingsport_dict['Central Hill'] = ['7th House on the Left','Congregational Hospital','St. Erasmus\'s Home']
        self.kingsport_dict['Harborside'] = ['607 Water St.','North Point Lighthouse','The Rope and Anchor']
        self.kingsport_dict['Kingsport Head'] = ['Strange High House','The Causeway','Wireless Station']
        self.kingsport_dict['South Shore'] = ['Artists\' Colony','Hall School','Neil\'s Curiosity Shop']
        self.kingsport_dict['Other Worlds'] = ['The Underworld','Unknown Kadath']
        self.locations_kingsport = sorted([value for key, value in self.kingsport_dict.items() if key not in ['Other Worlds']])
        self.streets_kingsport = sorted([key for key, value in self.kingsport_dict.items() if key not in ['Other Worlds']])
        self.otherWorlds_kingsport = sorted(self.kingsport_dict['Other Worlds'])

        self.innsmouth_dict = {}
        self.innsmouth_dict['Church Green'] = ['Esoteric Order of Dagon','Innsmouth Jail','Innsmouth: Jail Cell']
        self.innsmouth_dict['Factory District'] = ['First National Grocery','Gilman House Hotel','Marsh Refinery']
        self.innsmouth_dict['Innsmouth Shore'] = ['Devil Reef','Falcon Point','Y\'ha-nthlei']
        self.locations_innsmouth = sorted(list(self.innsmouth_dict.values()))
        self.streets_innsmouth = list(self.innsmouth_dict.keys())
        self.streets_innsmouth.append('Sawbone Alley')
        self.streets_innsmouth = self.streets_innsmouth.append('Joe Sargent\'s Bus Service')