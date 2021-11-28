# LINE Notify is Mond
ระบบแจ้งเตือนวันพระผ่าน Bot LINE Notify

## Setup
1. ทำการสร้าง Token LINE Notify ที่
https://notify-bot.line.me/en/

1. ติดตั้ง Library โดย library จะอยู่ใน requirements.txt ซึ่งสามารถพิมพ์คำสั่งได้ดังนี้
```
    pip install -r requirements.txt
```


3. เปลี่ยนชื่อ File ดังนี้
```
    config.example.json -> config.json
```

4. ทำการตั้งค่าใน Config โดยนำ Token ที่ได้หลังจากสร้าง Bot Notify จาก LINE แล้ว
```json
{
    "line": {
        "token": "ใส TOKEN ตรงนี้",
        "message": "....."
    }
}
```

5. ทำการตั้ง crontab ดังนี้ (**สำหรับ Linux**)
```
0 0 * * * /usr/bin/python3 <PATH_PYTHON_ALERT> --mond <PATH_MOND_PKL> --config <PATH_CONFIG_JSON>
```

ตัวอย่างการเขียน
```
0 0 * * * /usr/bin/python3 /home/m307/LINEALERT/mond/app/app.py --mond /home/m307/LINEALERT/mond/mond.pkl --config /home/m307/LINEALERT/mond/config.json
```

## Example
![Example Image](https://media.discordapp.net/attachments/751301184672890945/914437584514596925/unknown.png?width=364&height=127)

## Folder
| Folder | Description |
| :---: | :---: |
| service | เป็น Folder สำหรับ fetch วันพระ |
| app | เป็น Folder สำหรับแจ้งเตือนของ LINE Bot |

## License
MIT 

![ไม่มีอะไร](https://c.tenor.com/oZpbXQCEptMAAAAd/hu-tao-wave.gif)