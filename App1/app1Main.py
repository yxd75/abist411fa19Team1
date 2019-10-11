#Project: Project Diamond
#Purpose Details: Retrieve a JSON payload from the internet and send it to App2 using TLS. It will also retrieve an encrypted payload from App4 and save the JSON payload to a text file.
#Course: IST 411
#Author: Team 1
#Date Developed: 10/9/2019
#Last Date Changed: 
#Rev: 0


#This will call all other classes created, related to App1.
import sys
from PayloadRetriever import PayloadRetriever
from PayloadSaver import PayloadSaver


def main():

    print("Retrieving JSON payload from source.")
    payload = PayloadRetriever().readAndDecodeJSON()
    print("Sending payload to App2.")

    print("Saving payload to text file.")
    PayloadSaver().savePayload(payload)

    print("Not Finished")

if __name__ == '__main__':
    main()