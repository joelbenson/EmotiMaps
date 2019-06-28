
class StateUtilities():
    def getState(placeName, userLocation):
        state = ''
        #Try place name
        tuple = placeName.split(', ')
        if (len(tuple) > 1):
            state = tuple[1]
        if (len(state) == 2):
            return state
        #Otherwise, try user location
        tuple = userLocation.split(', ')
        if (len(tuple) > 1):
            state = tuple[1]
        if (len(state) == 2):
            return state
        #Given no location data, return NAS
        return "NAS"

    def getStateIndex(state):
        return{
            "AL": 0,
            "AK": 1,
            "AZ": 2,
            "AR": 3,
            "CA": 4,
            "CO": 5,
            "CT": 6,
            "DE": 7,
            "DC": 8,
            "FL": 9,
            "GA": 10,
            "HI": 11,
            "ID": 12,
            "IL": 13,
            "IN": 14,
            "IA": 15,
            "KS": 16,
            "KY": 17,
            "LA": 18,
            "ME": 19,
            "MD": 20,
            "MA": 21,
            "MI": 22,
            "MN": 23,
            "MS": 24,
            "MO": 25,
            "MT": 26,
            "NE": 27,
            "NV": 28,
            "NH": 29,
            "NJ": 30,
            "NM": 31,
            "NY": 32,
            "NC": 33,
            "ND": 34,
            "OH": 35,
            "OK": 36,
            "OR": 37,
            "PA": 38,
            "RI": 39,
            "SC": 40,
            "SD": 41,
            "TN": 42,
            "TX": 43,
            "UT": 44,
            "VT": 45,
            "VA": 46,
            "WA": 47,
            "WV": 48,
            "WI": 49,
            "WY": 50,
        }[state]

    def checkValidState(state):
        return{
            "AL": True,
            "AK": True,
            "AZ": True,
            "AR": True,
            "CA": True,
            "CO": True,
            "CT": True,
            "DE": True,
            "DC": True,
            "FL": True,
            "GA": True,
            "HI": True,
            "ID": True,
            "IL": True,
            "IN": True,
            "IA": True,
            "KS": True,
            "KY": True,
            "LA": True,
            "ME": True,
            "MD": True,
            "MA": True,
            "MI": True,
            "MN": True,
            "MS": True,
            "MO": True,
            "MT": True,
            "NE": True,
            "NV": True,
            "NH": True,
            "NJ": True,
            "NM": True,
            "NY": True,
            "NC": True,
            "ND": True,
            "OH": True,
            "OK": True,
            "OR": True,
            "PA": True,
            "RI": True,
            "SC": True,
            "SD": True,
            "TN": True,
            "TX": True,
            "UT": True,
            "VT": True,
            "VA": True,
            "WA": True,
            "WV": True,
            "WI": True,
            "WY": True,
        }.get(state, False)
