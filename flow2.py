[
    {
        "id": "65c34791.cea4d8",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "5fbd3daa.230614",
        "type": "http in",
        "z": "65c34791.cea4d8",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 140,
        "y": 200,
        "wires": [
            [
                "6ef69c0d.d06274",
                "1636a0b8.a57a3f"
            ]
        ]
    },
    {
        "id": "6ef69c0d.d06274",
        "type": "function",
        "z": "65c34791.cea4d8",
        "name": "Set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 360,
        "y": 200,
        "wires": [
            [
                "567be156.93d04"
            ]
        ]
    },
    {
        "id": "567be156.93d04",
        "type": "rpi-gpio out",
        "z": "65c34791.cea4d8",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 520,
        "y": 320,
        "wires": []
    },
    {
        "id": "1636a0b8.a57a3f",
        "type": "function",
        "z": "65c34791.cea4d8",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 360,
        "y": 100,
        "wires": [
            [
                "7dc24db5.104864",
                "8ba201b3.3a40c"
            ]
        ]
    },
    {
        "id": "7dc24db5.104864",
        "type": "http response",
        "z": "65c34791.cea4d8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 120,
        "wires": []
    },
    {
        "id": "8ba201b3.3a40c",
        "type": "debug",
        "z": "65c34791.cea4d8",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 750,
        "y": 280,
        "wires": []
    },
    {
        "id": "424104ae.43120c",
        "type": "http in",
        "z": "65c34791.cea4d8",
        "name": "Clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 110,
        "y": 380,
        "wires": [
            [
                "e8623679.3df5c8",
                "45566b56.6f3064"
            ]
        ]
    },
    {
        "id": "e8623679.3df5c8",
        "type": "function",
        "z": "65c34791.cea4d8",
        "name": "Clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 380,
        "wires": [
            [
                "567be156.93d04"
            ]
        ]
    },
    {
        "id": "45566b56.6f3064",
        "type": "function",
        "z": "65c34791.cea4d8",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 460,
        "wires": [
            [
                "7dc24db5.104864",
                "8ba201b3.3a40c"
            ]
        ]
    }
]
