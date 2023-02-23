
category = [
    "Select",
    "Technical Documentation",
    "Test Rigs",
    "Tooling//Fixture//Test Box",
    "Administrative",
    "Engineering Disposition",
    "External Communication",
    "Warranty//Red Bag"
]

task = [
        {"Admin":{
            "Training":[
                "Computer Based", 
                "Classroom", 
                "Offsite"
            ]
        }},
        {"Troubleshooting":{
            'ACT':[
                "MONR-ACT-001 GO-NOGO GAGE/ PRESSURE GAGE",
                "MONR-ACT-002 AMV RIG",
                "MONR-ACT-003 A310 TORQUE LIMITERS",
                "MONR-ACT-004 LOW STATIC PRESSURE",
                "MONR-ACT-005 THSA TEST BOX",
                "MONR-ACT-006 THSA TEST BOX",
                "MONR-ACT-007 UNIV TEST RIG",
                "MONR-ACT-008 THSA MODULE BOX",
                "MONR-ACT-009 YAW DAMPER",
                "MONR-ACT-010 A320 SERVO CONTROL",
                "MONR-ACT-011 PRESS",
                "MONR-ACT-012 LANDING GEAR ACTUATION TS",
                "MONR-ACT-014 STJE/TJE 0-5000 PSI PRESS XDUCERS",
                "MONR-ACT-015 UNIVERSAL SKYDROL ACTUATOR TEST RIG",
                "MONR-ACT-016 SERVO TEST RIG",
                "MONR-ACT-017 SERVO TEST BOX",
                "MONR-ACT-018 6-PORT UNIV TEST RIG",
                "MONR-ACT-019 THSA TEST RIG",
                "MONR-ACT-020 HYDRAULIC ACTUATORS",
                "MONR-ACT-021 MICRO-SWITCH TESTER",
                "MONR-ACT-022 4-PORT UNIV TEST RIG",
                "MONR-ACT-023 C12 FUEL PUMP TEST RIG",
                "MONR-ACT-024 THSA TEST BOX",
                "MONR-ACT-025 LG ACTUATOR TEST BOX",
                "MONR-ACT-026 A320 SERVO-CONTROL",
                "MONR-ACT-027 SERVO TEST BOX",
                "MONR-ACT-028 SERVO TEST BOX",
                "MONR-ACT-029 FLAP ACTUATOR",
                "MONR-ACT-030 A310 FLAP TEST RIG"
            ],
            "CARGO":[
                "MONR-CAR-001"
            ],
            "Heli":[
                "MONR-HES-001"
            ],
            "Vapo":[
                "MONR-VAP-001"
            ],
            "Rota":[
                "MONR-ROT-001"
            ],
            "Fans":[
                "MONR-FAN-001"
            ],
            "Hoist":[
                "MONR-HOW-001"
            ],
            "Starters":[
                "MONR-STR-001"
            ],
            "DeIcing":[
                "MONR-ICE-001"
            ],
            "Lighting":[
                "MONR-LIT-001"
            ],
            "New" :
            []
        }},
        {"project":{
            "active":[
            "Project A",
            "New Heli Rig",
            "TimeTracker"
        ],
            "inactive":[
                "THSA Rig"
            ]}
        }
    ]
engineers= {
        "home": {
                "Bill":["Shop", "user", "active", "Bill"],
                "Nate":["Rig", "user", "active", "Nate"],
                "sam":["Shop", "admin", "active", "Sam"],
                "Garrett":["Rig", "user", "active", "Garrett"],
                "Trevor":["Shop", "user", "active", "Trevor"]},
        "laptop": {
                "Bill":["Shop", "user", "active", "Bill"],
                "Nate":["Rig", "user", "active", "Nate"],
                "samsl":["Shop", "admin", "active", "Sam"],
                "Garrett":["Rig", "user", "active", "Garrett"],
                "Trevor":["Shop", "user", "active", "Trevor"],
                "Drew":["Shop", "user", "active", "Drew"],
                "Ezekiel":["Shop", "user", "active", "Ezekiel"],
                "Baha":["Shop", "user", "active", "Baha"],
                "Evan":["Shop", "user", "active", "Evan"]},
        "work": {
                "Bill":["Shop", "user", "active", "Bill"],
                "Nate":["Rig", "user", "active", "Nate"],
                "40001073":["Shop", "admin", "active", "Sam"],
                "Garrett":["Rig", "user", "active", "Garrett"],
                "Trevor":["Shop", "user", "active", "Trevor"]}
}
    
shopList = [
    "Actuation",
    "Landing Gear Structures",
    "Hoist and Winch",
    "Cargo",
    "Lighting",
    "DeIcing",
    "Vapor Cycle",
    "Rotatives",
    "Starters",
    "THSA",
    "HeliServo"
    "Test Rig and Validation"
]

shopCoverage ={
    "Sam":["Actuation", "Landing Gear Structures", "THSA"],
    "Trevor":["Hoist and Winch", "HeliServo"],
    "Drew":["Rotatives", "Starters"],
    "Ezekiel":["Vapor Cycle"],
    "Baha":["Cargo"],
    "Evan":["Lighting", "DeIcing"],
    "Other":["Test Rig and Validation"]
}
