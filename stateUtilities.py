from enum import Enum

class StateEnum(Enum):
    AL = 0
    AK = 1
    AZ = 2
    AR = 3
    CA = 4
    CO = 5
    CT = 6
    DE = 7
    DC = 8
    FL = 9
    GA = 10
    HI = 11
    ID = 12
    IL = 13
    IN = 14
    IA = 15
    KS = 16
    KY = 17
    LA = 18
    ME = 19
    MD = 20
    MA = 21
    MI = 22
    MN = 23
    MS = 24
    MO = 25
    MT = 26
    NE = 27
    NV = 28
    NH = 29
    NJ = 30
    NM = 31
    NY = 32
    NC = 33
    ND = 34
    OH = 35
    OK = 36
    OR = 37
    PA = 38
    RI = 39
    SC = 40
    SD = 41
    TN = 42
    TX = 43
    UT = 44
    VT = 45
    VA = 46
    WA = 47
    WV = 48
    WI = 49
    WY = 50

class StateUtilities():
    def getStateIndex(state):
        return{
            "AL": AL,
            "AK": AK,
            "AZ": AZ,
            "AR": AR,
            "CA": CA,
            "CO": CO,
            "CT": CT,
            "DE": DE,
            "DC": DC,
            "FL": FL,
            "GA": GA,
            "HI": HI,
            "ID": ID,
            "IL": IL,
            "IN": IN,
            "IA": IA,
            "KS": KS,
            "KY": KY,
            "LA": LA,
            "ME": ME,
            "MD": MD,
            "MA": MA,
            "MI": MI,
            "MN": MN,
            "MS": MS,
            "MO": MO,
            "MT": MT,
            "NE": NE,
            "NV": NV,
            "NH": NH,
            "NJ": NJ,
            "NM": NM,
            "NY": NY,
            "NC": NC,
            "ND": ND,
            "OH": OH,
            "OK": OK,
            "OR": OR,
            "PA": PA,
            "RI": RI,
            "SC": SC,
            "SD": SD,
            "TN": TN,
            "TX": TX,
            "UT": UT,
            "VT": VT,
            "VA": VA,
            "WA": WA,
            "WV": WV,
            "WI": WI,
            "WY": WY
        }[state]

    def getState(placeName, userLocation):
        state = ''
        #Try place name
        tuple = placeName.split(', ')
        if (len(tuple) > 1):
            state = tuple[1]
        if (len(state) == 2):
            return state
        #Try user location
        tuple = userLocation.split(', ')
        if (len(tuple) > 1):
            state = tuple[1]
        if (len(state) == 2):
            return state
        #Otherwise return NAS       
        return "NAS"
