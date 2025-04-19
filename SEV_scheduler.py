import heapq
from datetime import datetime

def time_to_min(t):
    return datetime.strptime(t, "%H:%M").hour * 60 + datetime.strptime(t, "%H:%M").minute

def min_to_time(m):
    return f"{m // 60:02d}:{m % 60:02d}"

buses = {
    1: [
        # Forward trips (Wesel → Oberhausen Hbf)
        {"stops": [{"station": "Wesel", "time": time_to_min("05:23")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("05:36")}, {"station": "Friedrichsfeld Post", "time": time_to_min("05:37")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("05:40")}, {"station": "Voerde", "time": time_to_min("05:50")}, {"station": "Dinslaken", "time": time_to_min("06:04")}, {"station": "OB-Holten", "time": time_to_min("06:05")}, {"station": "OB-Sterkrade", "time": time_to_min("06:17")}, {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("06:20")}]},
        {"stops": [{"station": "Wesel", "time": time_to_min("09:23")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("09:36")}, {"station": "Friedrichsfeld Post", "time": time_to_min("09:37")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("09:40")}, {"station": "Voerde", "time": time_to_min("09:50")}, {"station": "Dinslaken", "time": time_to_min("10:04")}, {"station": "OB-Holten", "time": time_to_min("10:05")}, {"station": "OB-Sterkrade", "time": time_to_min("10:17")}, {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("10:20")}]},
        {"stops": [{"station": "Wesel", "time": time_to_min("13:23")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("13:36")}, {"station": "Friedrichsfeld Post", "time": time_to_min("13:37")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("13:40")}, {"station": "Voerde", "time": time_to_min("13:50")}, {"station": "Dinslaken", "time": time_to_min("14:04")}, {"station": "OB-Holten", "time": time_to_min("14:05")}, {"station": "OB-Sterkrade", "time": time_to_min("14:17")}, {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("14:20")}]},
        {"stops": [{"station": "Wesel", "time": time_to_min("17:23")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("17:36")}, {"station": "Friedrichsfeld Post", "time": time_to_min("17:37")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("17:40")}, {"station": "Voerde", "time": time_to_min("17:50")}, {"station": "Dinslaken", "time": time_to_min("18:04")}, {"station": "OB-Holten", "time": time_to_min("18:05")}, {"station": "OB-Sterkrade", "time": time_to_min("18:17")}, {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("18:20")}]},
        # Return trips (Oberhausen Hbf → Wesel)
        {"stops": [{"station": "Oberhausen Hbf (RIM)", "time": time_to_min("07:20")}, {"station": "OB-Sterkrade", "time": time_to_min("07:34")}, {"station": "OB-Holten", "time": time_to_min("07:45")}, {"station": "Dinslaken", "time": time_to_min("08:01")}, {"station": "Voerde", "time": time_to_min("08:12")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("08:22")}, {"station": "Friedrichsfeld Post", "time": time_to_min("08:24")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("08:25")}, {"station": "Wesel", "time": time_to_min("08:40")}]},
        {"stops": [{"station": "Oberhausen Hbf (RIM)", "time": time_to_min("11:20")}, {"station": "OB-Sterkrade", "time": time_to_min("11:34")}, {"station": "OB-Holten", "time": time_to_min("11:45")}, {"station": "Dinslaken", "time": time_to_min("12:01")}, {"station": "Voerde", "time": time_to_min("12:12")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("12:22")}, {"station": "Friedrichsfeld Post", "time": time_to_min("12:24")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("12:25")}, {"station": "Wesel", "time": time_to_min("12:40")}]},
        {"stops": [{"station": "Oberhausen Hbf (RIM)", "time": time_to_min("15:20")}, {"station": "OB-Sterkrade", "time": time_to_min("15:34")}, {"station": "OB-Holten", "time": time_to_min("15:45")}, {"station": "Dinslaken", "time": time_to_min("16:01")}, {"station": "Voerde", "time": time_to_min("16:12")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("16:22")}, {"station": "Friedrichsfeld Post", "time": time_to_min("16:24")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("16:25")}, {"station": "Wesel", "time": time_to_min("16:40")}]},
        {"stops": [{"station": "Oberhausen Hbf (RIM)", "time": time_to_min("19:20")}, {"station": "OB-Sterkrade", "time": time_to_min("19:34")}, {"station": "OB-Holten", "time": time_to_min("19:45")}, {"station": "Dinslaken", "time": time_to_min("20:01")}, {"station": "Voerde", "time": time_to_min("20:12")}, {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("20:22")}, {"station": "Friedrichsfeld Post", "time": time_to_min("20:24")}, {"station": "Friedrichsfeld (alt)", "time": time_to_min("20:25")}, {"station": "Wesel", "time": time_to_min("20:40")}]}
    ],
    2: [
        # Forward trips (Wesel → Oberhausen Hbf)
        {"stops": [
            {"station": "Wesel", "time": time_to_min("06:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("06:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("06:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("06:40")},
            {"station": "Voerde", "time": time_to_min("06:50")},
            {"station": "Dinslaken", "time": time_to_min("07:04")},
            {"station": "OB-Holten", "time": time_to_min("07:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("07:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("07:46")}
        ]},
        {"stops": [
            {"station": "Wesel", "time": time_to_min("10:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("10:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("10:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("10:40")},
            {"station": "Voerde", "time": time_to_min("10:50")},
            {"station": "Dinslaken", "time": time_to_min("11:04")},
            {"station": "OB-Holten", "time": time_to_min("11:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("11:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("11:46")}
        ]},
        
        # Return trips (Oberhausen Hbf → Wesel)
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("08:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("08:34")},
            {"station": "OB-Holten", "time": time_to_min("08:45")},
            {"station": "Dinslaken", "time": time_to_min("09:01")},
            {"station": "Voerde", "time": time_to_min("09:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("09:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("09:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("09:25")},
            {"station": "Wesel", "time": time_to_min("09:40")}
        ]},
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("12:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("12:34")},
            {"station": "OB-Holten", "time": time_to_min("12:45")},
            {"station": "Dinslaken", "time": time_to_min("13:01")},
            {"station": "Voerde", "time": time_to_min("13:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("13:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("13:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("13:25")},
            {"station": "Wesel", "time": time_to_min("13:40")}
        ]}
    ],

    3: [
        # Forward trips (Emmerich → Oberhausen Hbf)
        {"stops": [
            {"station": "Emmerich", "time": time_to_min("06:13")},
            {"station": "Praest", "time": time_to_min("06:21")},
            {"station": "Millingen", "time": time_to_min("06:28")},
            {"station": "Empel-Rees", "time": time_to_min("06:37")},
            {"station": "Haldern", "time": time_to_min("06:44")},
            {"station": "Mehrhoog", "time": time_to_min("06:53")},
            {"station": "Wesel-Feldmark", "time": time_to_min("07:07")},
            {"station": "Wesel", "time": time_to_min("07:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("07:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("07:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("07:40")},
            {"station": "Voerde", "time": time_to_min("07:50")},
            {"station": "Dinslaken", "time": time_to_min("08:04")},
            {"station": "OB-Holten", "time": time_to_min("08:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("08:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("08:46")}
        ]},
        {"stops": [
            {"station": "Wesel", "time": time_to_min("11:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("11:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("11:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("11:40")},
            {"station": "Voerde", "time": time_to_min("11:50")},
            {"station": "Dinslaken", "time": time_to_min("12:04")},
            {"station": "OB-Holten", "time": time_to_min("12:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("12:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("12:46")}
        ]},
        {"stops": [
            {"station": "Wesel", "time": time_to_min("15:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("15:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("15:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("15:40")},
            {"station": "Voerde", "time": time_to_min("15:50")},
            {"station": "Dinslaken", "time": time_to_min("16:04")},
            {"station": "OB-Holten", "time": time_to_min("16:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("16:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("16:46")}
        ]},
        
        # Return trips (Oberhausen Hbf → Emmerich)
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("09:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("09:34")},
            {"station": "OB-Holten", "time": time_to_min("09:45")},
            {"station": "Dinslaken", "time": time_to_min("10:01")},
            {"station": "Voerde", "time": time_to_min("10:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("10:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("10:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("10:25")},
            {"station": "Wesel", "time": time_to_min("10:40")},
        ]},
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("13:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("13:34")},
            {"station": "OB-Holten", "time": time_to_min("13:45")},
            {"station": "Dinslaken", "time": time_to_min("14:01")},
            {"station": "Voerde", "time": time_to_min("14:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("14:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("14:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("14:25")},
            {"station": "Wesel", "time": time_to_min("14:40")},
        ]},
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("17:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("17:34")},
            {"station": "OB-Holten", "time": time_to_min("17:45")},
            {"station": "Dinslaken", "time": time_to_min("18:01")},
            {"station": "Voerde", "time": time_to_min("18:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("18:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("18:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("18:25")},
            {"station": "Wesel", "time": time_to_min("18:40")},
        ]}
    ],

    4: [
        # Forward trips (Wesel → Oberhausen Hbf)
        {"stops": [
            {"station": "Wesel", "time": time_to_min("08:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("08:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("08:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("08:40")},
            {"station": "Voerde", "time": time_to_min("08:50")},
            {"station": "Dinslaken", "time": time_to_min("09:04")},
            {"station": "OB-Holten", "time": time_to_min("09:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("09:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("09:46")}
        ]},
        {"stops": [
            {"station": "Wesel", "time": time_to_min("12:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("12:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("12:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("12:40")},
            {"station": "Voerde", "time": time_to_min("12:50")},
            {"station": "Dinslaken", "time": time_to_min("13:04")},
            {"station": "OB-Holten", "time": time_to_min("13:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("13:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("13:46")}
        ]},
        {"stops": [
            {"station": "Wesel", "time": time_to_min("16:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("16:36")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("16:37")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("16:40")},
            {"station": "Voerde", "time": time_to_min("16:50")},
            {"station": "Dinslaken", "time": time_to_min("17:04")},
            {"station": "OB-Holten", "time": time_to_min("17:19")},
            {"station": "OB-Sterkrade", "time": time_to_min("17:31")},
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("17:46")}
        ]},
        
        # Return trips (Oberhausen Hbf → Wesel)
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("06:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("06:34")},
            {"station": "OB-Holten", "time": time_to_min("06:45")},
            {"station": "Dinslaken", "time": time_to_min("07:01")},
            {"station": "Voerde", "time": time_to_min("07:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("07:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("07:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("07:25")},
            {"station": "Wesel", "time": time_to_min("07:40")}
        ]},
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("10:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("10:34")},
            {"station": "OB-Holten", "time": time_to_min("10:45")},
            {"station": "Dinslaken", "time": time_to_min("11:01")},
            {"station": "Voerde", "time": time_to_min("11:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("11:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("11:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("11:25")},
            {"station": "Wesel", "time": time_to_min("11:40")}
        ]},
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("14:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("14:34")},
            {"station": "OB-Holten", "time": time_to_min("14:45")},
            {"station": "Dinslaken", "time": time_to_min("15:01")},
            {"station": "Voerde", "time": time_to_min("15:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("15:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("15:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("15:25")},
            {"station": "Wesel", "time": time_to_min("15:40")}
        ]},
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("18:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("18:34")},
            {"station": "OB-Holten", "time": time_to_min("18:45")},
            {"station": "Dinslaken", "time": time_to_min("19:01")},
            {"station": "Voerde", "time": time_to_min("19:12")},
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("19:22")},
            {"station": "Friedrichsfeld Post", "time": time_to_min("19:24")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("19:25")},
            {"station": "Wesel", "time": time_to_min("19:40")}
        ]}
    ],

    5: [
        # Einzige Hin-Fahrt (Wesel → Oberhausen Hbf)
        {"stops": [
            {"station": "Wesel", "time": time_to_min("14:23")},
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("14:36")},  # +13 min
            {"station": "Friedrichsfeld Post", "time": time_to_min("14:37")},   # +1 min
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("14:40")}, # +3 min
            {"station": "Voerde", "time": time_to_min("14:50")},                # +10 min
            {"station": "Dinslaken", "time": time_to_min("15:04")},             # +14 min
            {"station": "OB-Holten", "time": time_to_min("15:19")},             # +15 min
            {"station": "OB-Sterkrade", "time": time_to_min("15:31")},          # +12 min
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("15:46")}   # +15 min
        ]},

        # Einzige Rückfahrt (Oberhausen Hbf → Wesel)
        {"stops": [
            {"station": "Oberhausen Hbf (RIM)", "time": time_to_min("16:20")},
            {"station": "OB-Sterkrade", "time": time_to_min("16:34")},          # +14 min
            {"station": "OB-Holten", "time": time_to_min("16:45")},             # +11 min
            {"station": "Dinslaken", "time": time_to_min("17:01")},             # +16 min
            {"station": "Voerde", "time": time_to_min("17:12")},                # +11 min
            {"station": "Friedrichsfeld (Ersatz)", "time": time_to_min("17:22")}, # +10 min
            {"station": "Friedrichsfeld Post", "time": time_to_min("17:24")},   # +2 min
            {"station": "Friedrichsfeld (alt)", "time": time_to_min("17:25")},  # +1 min
            {"station": "Wesel", "time": time_to_min("17:40")}                  # +15 min
        ]}
    ],

    81: [
        # Dinslaken → Duisburg Hbf
        {"stops": [{"station": "Dinslaken", "time": time_to_min("06:30")}, {"station": "Duisburg Hbf", "time": time_to_min("07:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("08:10")}, {"station": "Duisburg Hbf", "time": time_to_min("08:40")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("09:50")}, {"station": "Duisburg Hbf", "time": time_to_min("10:20")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("11:30")}, {"station": "Duisburg Hbf", "time": time_to_min("12:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("13:10")}, {"station": "Duisburg Hbf", "time": time_to_min("13:40")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("14:50")}, {"station": "Duisburg Hbf", "time": time_to_min("15:20")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("16:30")}, {"station": "Duisburg Hbf", "time": time_to_min("17:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("18:10")}, {"station": "Duisburg Hbf", "time": time_to_min("18:40")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("20:00")}, {"station": "Duisburg Hbf", "time": time_to_min("20:30")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("21:30")}, {"station": "Duisburg Hbf", "time": time_to_min("22:00")}]},
        # Duisburg Hbf → Dinslaken
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("05:45")}, {"station": "Dinslaken", "time": time_to_min("06:15")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("07:25")}, {"station": "Dinslaken", "time": time_to_min("07:55")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("09:05")}, {"station": "Dinslaken", "time": time_to_min("09:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("10:45")}, {"station": "Dinslaken", "time": time_to_min("11:15")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("12:25")}, {"station": "Dinslaken", "time": time_to_min("12:55")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("14:05")}, {"station": "Dinslaken", "time": time_to_min("14:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("15:45")}, {"station": "Dinslaken", "time": time_to_min("16:15")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("17:25")}, {"station": "Dinslaken", "time": time_to_min("17:55")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("19:05")}, {"station": "Dinslaken", "time": time_to_min("19:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("20:35")}, {"station": "Dinslaken", "time": time_to_min("21:05")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("22:05")}, {"station": "Dinslaken", "time": time_to_min("22:35")}]}
    ],

    82: [
        # Dinslaken → Duisburg Hbf (Mo-Fr)
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("05:30")},
            {"station": "Duisburg Hbf", "time": time_to_min("06:00")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("06:50")},  # Fahrtnummer 8049006
            {"station": "Duisburg Hbf", "time": time_to_min("07:20")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("08:30")},  # 8049016
            {"station": "Duisburg Hbf", "time": time_to_min("09:00")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("10:10")},  # 8049072
            {"station": "Duisburg Hbf", "time": time_to_min("10:40")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("11:50")},  # 8049058
            {"station": "Duisburg Hbf", "time": time_to_min("12:20")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("13:30")},  # 8049030
            {"station": "Duisburg Hbf", "time": time_to_min("14:00")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("15:10")},  # 8049082
            {"station": "Duisburg Hbf", "time": time_to_min("15:40")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("16:50")},  # 8049068
            {"station": "Duisburg Hbf", "time": time_to_min("17:20")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("18:30")},  # 8049040
            {"station": "Duisburg Hbf", "time": time_to_min("19:00")}
        ]},

        # Duisburg Hbf → Dinslaken (Mo-Fr)
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("06:05")},  # 8049005
            {"station": "Dinslaken", "time": time_to_min("06:35")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("07:45")},  # 8049015
            {"station": "Dinslaken", "time": time_to_min("08:15")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("09:25")},  # 8049025
            {"station": "Dinslaken", "time": time_to_min("09:55")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("11:05")},  # 8049031
            {"station": "Dinslaken", "time": time_to_min("11:35")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("12:45")},  # 8049085
            {"station": "Dinslaken", "time": time_to_min("13:15")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("14:25")},  # 8049071
            {"station": "Dinslaken", "time": time_to_min("14:55")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("16:05")},  # 8049041
            {"station": "Dinslaken", "time": time_to_min("16:35")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("17:45")},  # 8049095
            {"station": "Dinslaken", "time": time_to_min("18:15")}
        ]}
    ],

    83: [
        # Dinslaken → Duisburg Hbf (Mo-Fr)
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("05:50")},  # Fahrt 8049052
            {"station": "Duisburg Hbf", "time": time_to_min("06:20")}  # +30 min
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("07:10")},  # 8049008
            {"station": "Duisburg Hbf", "time": time_to_min("07:40")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("08:50")},  # 8049018
            {"station": "Duisburg Hbf", "time": time_to_min("09:20")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("10:30")},  # 8049024
            {"station": "Duisburg Hbf", "time": time_to_min("11:00")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("12:10")},  # 8049076
            {"station": "Duisburg Hbf", "time": time_to_min("12:40")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("13:50")},  # 8049062
            {"station": "Duisburg Hbf", "time": time_to_min("14:20")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("15:30")},  # 8049034
            {"station": "Duisburg Hbf", "time": time_to_min("16:00")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("17:10")},  # 8049086
            {"station": "Duisburg Hbf", "time": time_to_min("17:40")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("19:00")},  # 8049042
            {"station": "Duisburg Hbf", "time": time_to_min("19:30")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("20:30")},  # 8049048
            {"station": "Duisburg Hbf", "time": time_to_min("21:00")}
        ]},
        {"stops": [
            {"station": "Dinslaken", "time": time_to_min("22:00")},  # 8049112
            {"station": "Duisburg Hbf", "time": time_to_min("22:30")}
        ]},

        # Duisburg Hbf → Dinslaken (Mo-Fr)
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("05:05")},  # 8049057
            {"station": "Dinslaken", "time": time_to_min("05:35")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("06:25")},  # 8049007
            {"station": "Dinslaken", "time": time_to_min("06:55")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("08:05")},  # 8049017
            {"station": "Dinslaken", "time": time_to_min("08:35")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("09:45")},  # 8049027
            {"station": "Dinslaken", "time": time_to_min("10:15")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("11:25")},  # 8049065
            {"station": "Dinslaken", "time": time_to_min("11:55")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("13:05")},  # 8049035
            {"station": "Dinslaken", "time": time_to_min("13:35")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("14:45")},  # 8049089
            {"station": "Dinslaken", "time": time_to_min("15:15")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("16:25")},  # 8049075
            {"station": "Dinslaken", "time": time_to_min("16:55")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("18:05")},  # 8049045
            {"station": "Dinslaken", "time": time_to_min("18:35")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("19:35")},  # 8049053
            {"station": "Dinslaken", "time": time_to_min("20:05")}
        ]},
        {"stops": [
            {"station": "Duisburg Hbf", "time": time_to_min("21:05")},  # 8049117
            {"station": "Dinslaken", "time": time_to_min("21:35")}
        ]}
    ],

    84: [
        # Dinslaken → Duisburg Hbf (Hinfahrten)
        {"stops": [{"station": "Dinslaken", "time": time_to_min("06:10")}, {"station": "Duisburg Hbf", "time": time_to_min("06:40")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("07:30")}, {"station": "Duisburg Hbf", "time": time_to_min("08:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("09:10")}, {"station": "Duisburg Hbf", "time": time_to_min("09:40")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("10:30")}, {"station": "Duisburg Hbf", "time": time_to_min("11:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("12:30")}, {"station": "Duisburg Hbf", "time": time_to_min("13:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("13:30")}, {"station": "Duisburg Hbf", "time": time_to_min("14:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("15:00")}, {"station": "Duisburg Hbf", "time": time_to_min("15:30")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("16:30")}, {"station": "Duisburg Hbf", "time": time_to_min("17:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("17:30")}, {"station": "Duisburg Hbf", "time": time_to_min("18:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("19:30")}, {"station": "Duisburg Hbf", "time": time_to_min("20:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("21:00")}, {"station": "Duisburg Hbf", "time": time_to_min("21:30")}]},

        # Duisburg Hbf → Dinslaken (Rückfahrten)
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("06:45")}, {"station": "Dinslaken", "time": time_to_min("07:15")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("07:45")}, {"station": "Dinslaken", "time": time_to_min("08:15")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("09:25")}, {"station": "Dinslaken", "time": time_to_min("09:55")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("11:05")}, {"station": "Dinslaken", "time": time_to_min("11:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("12:35")}, {"station": "Dinslaken", "time": time_to_min("13:05")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("14:05")}, {"station": "Dinslaken", "time": time_to_min("14:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("15:35")}, {"station": "Dinslaken", "time": time_to_min("16:05")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("17:05")}, {"station": "Dinslaken", "time": time_to_min("17:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("18:35")}, {"station": "Dinslaken", "time": time_to_min("19:05")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("20:05")}, {"station": "Dinslaken", "time": time_to_min("20:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("21:35")}, {"station": "Dinslaken", "time": time_to_min("22:05")}]}
    ],

    85: [
        # Hinfahrten (Dinslaken → Duisburg Hbf)
        {"stops": [{"station": "Dinslaken", "time": time_to_min("07:50")}, {"station": "Duisburg Hbf", "time": time_to_min("08:20")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("09:30")}, {"station": "Duisburg Hbf", "time": time_to_min("10:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("11:10")}, {"station": "Duisburg Hbf", "time": time_to_min("11:40")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("12:50")}, {"station": "Duisburg Hbf", "time": time_to_min("13:20")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("14:30")}, {"station": "Duisburg Hbf", "time": time_to_min("15:00")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("16:10")}, {"station": "Duisburg Hbf", "time": time_to_min("16:40")}]},
        {"stops": [{"station": "Dinslaken", "time": time_to_min("17:50")}, {"station": "Duisburg Hbf", "time": time_to_min("18:20")}]},

        # Rückfahrten (Duisburg Hbf → Dinslaken)
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("07:05")}, {"station": "Dinslaken", "time": time_to_min("07:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("08:45")}, {"station": "Dinslaken", "time": time_to_min("09:15")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("10:25")}, {"station": "Dinslaken", "time": time_to_min("10:55")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("12:05")}, {"station": "Dinslaken", "time": time_to_min("12:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("13:45")}, {"station": "Dinslaken", "time": time_to_min("14:15")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("15:25")}, {"station": "Dinslaken", "time": time_to_min("15:55")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("17:05")}, {"station": "Dinslaken", "time": time_to_min("17:35")}]},
        {"stops": [{"station": "Duisburg Hbf", "time": time_to_min("18:45")}, {"station": "Dinslaken", "time": time_to_min("19:15")}]},
    ]

}

class State:
    def __init__(self, current_time, location, checked, path):
        self.current_time = current_time
        self.location = location
        self.checked = frozenset(checked)
        self.path = path

    def __lt__(self, other):
        return self.current_time < other.current_time

def find_optimal_schedule(start_time, start_location, buses):
    counter = 0
    heap = []
    visited = {}
    initial = State(time_to_min(start_time), start_location, set(), [])
    heapq.heappush(heap, (initial.current_time, counter, initial))
    counter += 1
    best = None

    while heap:
        current_time, _, state = heapq.heappop(heap)
        
        if best and current_time >= best.current_time:
            continue

        key = (state.location, state.checked)
        if key in visited and visited[key] <= current_time:
            continue
        visited[key] = current_time

        if len(state.checked) == len(buses):
            if not best or current_time < best.current_time:
                best = state
            continue

        # Busfahrten hinzufügen
        for bus_id, trips in buses.items():
            if bus_id in state.checked:
                continue
            for trip in trips:
                for i in range(len(trip["stops"]) - 1):
                    stop = trip["stops"][i]
                    next_stop = trip["stops"][i + 1]
                    if stop["station"] == state.location and stop["time"] >= current_time:
                        new_checked = set(state.checked)
                        new_checked.add(bus_id)
                        new_state = State(
                            next_stop["time"],
                            next_stop["station"],
                            new_checked,
                            state.path + [{
                                "bus": bus_id,
                                "from": stop["station"],
                                "to": next_stop["station"],
                                "start": min_to_time(stop["time"]),
                                "end": min_to_time(next_stop["time"])
                            }]
                        )
                        heapq.heappush(heap, (new_state.current_time, counter, new_state))
                        counter += 1

        # Umstieg an der gleichen Haltestelle mit Wartezeit
        if len(state.path) < 5:
            new_location = state.location  # Haltestelle bleibt gleich
            transfer_time = 0  # Realistische Wartezeit von 15 Minuten
            new_state = State(
                current_time + transfer_time,
                new_location,
                state.checked,
                state.path.copy()
            )
            heapq.heappush(heap, (new_state.current_time, counter, new_state))
            counter += 1

    return best

# Test
start_time = "11:00"
best_solution = find_optimal_schedule(start_time, "Duisburg Hbf", buses)
if best_solution:
    print("Optimaler Plan:")
    for step in best_solution.path:
        print(f"Bus {step['bus']}: {step['from']} ({step['start']}) → {step['to']} ({step['end']})")
    print(f"Gesamtdauer (bisher falsche berechnung!): {min_to_time(best_solution.current_time - time_to_min(start_time))}")
else:
    print("Keine Lösung gefunden.")

print("----------------------")

best_solution = find_optimal_schedule(start_time, "Dinslaken", buses)
if best_solution:
    print("Optimaler Plan:")
    for step in best_solution.path:
        print(f"Bus {step['bus']}: {step['from']} ({step['start']}) → {step['to']} ({step['end']})")
    print(f"Gesamtdauer (bisher falsche berechnung!): {min_to_time(best_solution.current_time - time_to_min(start_time))}")
else:
    print("Keine Lösung gefunden.")