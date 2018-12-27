[
    {
        "id": "5765dfba.822c5",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "cdeacd69.73dd",
        "type": "http in",
        "z": "5765dfba.822c5",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 190,
        "y": 220,
        "wires": [
            [
                "14729dab.583962"
            ]
        ]
    },
    {
        "id": "58b52a61.af7b84",
        "type": "rpi-gpio in",
        "z": "5765dfba.822c5",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 190,
        "y": 400,
        "wires": [
            [
                "3ec73208.4c456e"
            ]
        ]
    },
    {
        "id": "3ec73208.4c456e",
        "type": "function",
        "z": "5765dfba.822c5",
        "name": "SET GPIO",
        "func": "global.set(\"GPIO\",msg.payload);\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 390,
        "y": 300,
        "wires": [
            [
                "fc6fdce1.03d09"
            ]
        ]
    },
    {
        "id": "14729dab.583962",
        "type": "function",
        "z": "5765dfba.822c5",
        "name": "GET GPIO",
        "func": "msg.payload=global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 390,
        "y": 220,
        "wires": [
            [
                "f2d64f56.d41e4",
                "fc6fdce1.03d09"
            ]
        ]
    },
    {
        "id": "f2d64f56.d41e4",
        "type": "http response",
        "z": "5765dfba.822c5",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 660,
        "y": 240,
        "wires": []
    },
    {
        "id": "fc6fdce1.03d09",
        "type": "debug",
        "z": "5765dfba.822c5",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 620,
        "y": 380,
        "wires": []
    }
]
