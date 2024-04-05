import time


def customCallback(client, userdata, message):
    print("callback came...")
    print(message.payload)


from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

myMQTTClient = AWSIoTMQTTClient("vibration_sensor")
myMQTTClient.configureEndpoint("alav9gkz2nm5p-ats.iot.ap-south-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials(
    "AmazonRootCA1.pem",
    "a3c4001b354a387d2e3215c52e9dd8b1a3007f7431cf33dc1e094fafca819584-private.pem.key",
    "a3c4001b354a387d2e3215c52e9dd8b1a3007f7431cf33dc1e094fafca819584-certificate.pem.crt",
)

myMQTTClient.connect()
print("Client Connected")

myMQTTClient.subscribe("general/outbound", 1, customCallback)
print("waiting for the callback. Click to conntinue...")
x = input()

myMQTTClient.unsubscribe("general/outbound")
print("Client unsubscribed")


myMQTTClient.disconnect()
print("Client Disconnected")
