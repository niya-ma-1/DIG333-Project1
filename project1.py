    from gpiozero import MotionSensor, LED
    import time
    from io import BytesIO
    from gtts import gTTS
    import os
    import requests

    green_led = LED(17)
    pir = MotionSensor(4)
    green_led.off()


    def compliment():
        response = requests.get("https://complimentr.com/api")
        mytext = response.json()['compliment']

        response_temp = requests.get("http://api.weatherapi.com/v1/current.json?key=26bded3797e543e38be180501231603&q=Charlotte&aqi=no")
        mytext_temp = response_temp.json()['current']['temp_f']

        language = 'en'
        mytext = "Temperature outside is " + str(mytext_temp) + " fahrenheit. " + mytext

        print(mytext)
        tts = gTTS(text=mytext, lang=language, slow=False)
        tts.save('test.mp3')

        time.sleep(1)
        os.system("mplayer -volume 50 test.mp3")


    while True:
        pir.wait_for_motion()
        print("Motion Detected")
        compliment()

        green_led.on()
        pir.wait_for_no_motion()
        green_led.off()
        print("Motion Stopped")
