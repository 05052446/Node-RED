[
    {
        "id": "78d1a3ff.d2c97c",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "6c4bbe23.7b65",
        "type": "inject",
        "z": "78d1a3ff.d2c97c",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 150,
        "y": 200,
        "wires": [
            [
                "b939bf4e.f7a9d"
            ]
        ]
    },
    {
        "id": "b939bf4e.f7a9d",
        "type": "function",
        "z": "78d1a3ff.d2c97c",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey:\"yqr2tLTG1YU0lW7i\"\n};\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 240,
        "wires": [
            [
                "5299a961.db7be8",
                "7f619351.77dd3c"
            ]
        ]
    },
    {
        "id": "5299a961.db7be8",
        "type": "http request",
        "z": "78d1a3ff.d2c97c",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/D7GS6880/datachannels/Temperature/datapoints.csv",
        "tls": "",
        "x": 510,
        "y": 220,
        "wires": [
            [
                "17fc1dbf.14c552",
                "13e1e40e.53042c"
            ]
        ]
    },
    {
        "id": "7f619351.77dd3c",
        "type": "http request",
        "z": "78d1a3ff.d2c97c",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/D7GS6880/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 510,
        "y": 280,
        "wires": [
            [
                "17fc1dbf.14c552",
                "13e1e40e.53042c"
            ]
        ]
    },
    {
        "id": "17fc1dbf.14c552",
        "type": "http response",
        "z": "78d1a3ff.d2c97c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 740,
        "y": 220,
        "wires": []
    },
    {
        "id": "13e1e40e.53042c",
        "type": "debug",
        "z": "78d1a3ff.d2c97c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 740,
        "y": 320,
        "wires": []
    }
]
