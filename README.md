# trickortreatmachine
This is a fun project that uses a RaspberryPi Model B+ v1.2, a few basic python scripts, and a windshiled wiper motor to create a trick or treat machine!

https://youtube.com/shorts/2BGu9tIV1tE?feature=share

# How does it work?


# Requirements
 - RPi Model B+ v1.2
 - Twitter Developer Account with API Access, [More Information here](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/api-key-and-secret)
 - Relay
 - Servo Motor
 - RPi Camera
 - Winshield Wiper Motor
 - Button x2
 - speakers


# Operation
## Install dependencies

Install PIP
```
sudo apt install python3-pip
```

Install python libraries
```
python3 -m pip install -r python-requirements.txt
```

## Create a secrets file to store API credentials
Create `secrets.py` with twitter API credentials
```
cp secrets.py.sample secrets.py
```

Modify Contents with your API credentials, example
```
#Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

## (Optional) Modify paramaters
Modify `config.py` if changes are desired, like new GPIO PIN numbers or different sound files

### Variables
- `relay` Defines pin for activating relay, aka move the winshield wiper motor
- `servo` SPIO pin that is connected to the servo motor
- `trickinput` GPIO pin connected to button that will activate the trick function
- `treatinput` GPIO pin connected to button that will activate the treat function
- `tricksound1` path to first sound played in trick function
- `tricksound2` path to second sound played in trick function
- `treatsound1` path to first sound played in treat function
- `treatsound2` path to second sound played in treat function
- `treatsound3` path to thrid sound played in treat function


## Make Connections

connection diagram goes here


## Run python script
Fill the candy bucket! and run the following command to start the fun

```
python3 main.py
```





