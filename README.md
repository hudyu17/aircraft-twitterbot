# aircraft-twitterbot

*Inspired by [ElonJet](https://twitter.com/ElonJet)*

This twitterbot tweets an image of all airborne Cathay Pacific aircraft every hour.

## but why tho

1. Watched Fireship's [video](https://www.youtube.com/watch?v=bJUl3OAIT0k&ab_channel=Fireship) on how a uni student made a twitterbot to track Elon Musk's private plane - immediately thought "how hard could it be" (it was a lil hard) 

2. I like planes ([shoutout to The Flying Moose](https://www.youtube.com/channel/UCC2b7zRRgBDAK6QSiqOrdPQ)) and Cathay Pacific + CX have really struggled during COVID → wanted to give people a a friendly reminder that this airline is still alive :^)

## How it works:
- Cycles through all icao24 numbers of Cathay's fleet
- Calls the [open sky API](https://openskynetwork.github.io/opensky-api/rest.html) to retrieve current state of all aircraft
- If aircraft are airborne, creates a staticmap and tweets it
- Repeat every hour (currently off)
