# Prize Categories
## Best Open Source
**Multi-Factor authentication (MFA) Security Key - 4 winners**
This award recognizes projects that present the best utilization of open-source software, tools, or contributions.
## Best Game Hack
**Mechanical Keyboard - 4 winners**
This award recognizes the best game developed during the hackathon (that includes our feathered friends!), emphasizing creativity, gameplay, technical implementation, and player experience.

## \[MLH\] Best Use of Tiger Data
**Stream Deck Mini - 1 winner**
Building high-performance apps under hackathon deadlines shouldn't mean spending half your weekend configuring complex databases or learning obscure query languages. Tiger Data extends PostgreSQL to give student developers an ultra-fast foundation for real-time data, time-series metrics, and complex analytics.

Why build with Tiger Data this weekend?

Standard SQL Power: Query massive datasets instantly using the SQL you already know, with no complex NoSQL aggregation pipelines required.

Unified Data Stack: Store relational user profiles and high-frequency metric streams side-by-side in a single database.

Instant Dashboards: Serve lag-free, real-time frontend charts using pre-computed Continuous Aggregates.

90%+ Data Compression: Store millions of events on free-tier cloud instances without running out of disk space.

Whether you’re building real-time IoT monitoring, AI-driven analytics dashboards, or financial prediction engines, show us how Tiger Data powers your project. The team that demonstrates the most innovative, impactful, and performance-driven use of Tiger Data will take home some great prizes!

# Ideas
## RIT SDK
A way to connect many different RIT data endpoints together.

### Endpoints

- RIT EMS Outlook API
- Tripshot Live bus location
- myCourses assignment information or todo list
- HA dashboard integration? (if time)
- Playwright data extraction of other sites (ServiceNow)

# Brainstorming

First up: RIT shibboleth auth as root class
most service modules descend from this for authentication with exception of tripshot

distinction of user/public service modules and "add-ons"

**Public Service Modules**: RIT resources that are public, don't require auth

**User Service Modules**: RIT resources that require authentication to interact with, behind shibboleth

**External Service Modules**: Non-RIT resources (external personal auth) 

### Public Service Modules

- Dining hours
- Visiting chefs

### User Service Modules

- EMS
- myCourses

### External Service Modules

- TripShot

### Homeassistant Controller

Custom integration that will show all of the retrieved data from different APIs. This module would need to pull new data from certain APIs like tripshot so that every interval (10 seconds) it gets updated data of a bus route for example.

To Operate:
- Push notifications for alerts to a phone
- HA Display cards for interfacing
    - Bus arrival time
    - Todo cards
    - Max75 displays (w/ ESPHome) [extra]

### Mycourses Calendar Exporting

Playwright needs to go into any "Active" non-closed classes that have a valid calendar tab (like a standard course). Go to the subscriptions tab and export the link. A valid link looks like the following:
`https://mycourses.rit.edu/d2l/le/calendar/feed/user/feed.ics?token=...`

Calander links should be stored for the user to see in someway, static config is fine. Should be added to homeassistant calendar with a tag. Tagged courses should fire a reminder when a configurable deadline is passed like 2 hours.


# Tasks to do (as of Sun 12 AM)

- [ ] Write global variable configs for polling intervals available in homeassistant
- [ ] 



# Devpost

## Inspiration

We wanted to build something that would be of immediate use and could help students that want to develop applications interface with data from RIT. We are both active members in the RIT FOSS community and wanted to make something that other students can use and build on top of.

## What does it do?

RIT SDK is a series of connectors and endpoints that is able to pull data from many different services that RIT has. We able to pull data from the following sources:

- Tripshot Live bus location
- myCourses assignment calendar
- Playwright data extraction of other sites (ServiceNow)?
- 

The base SDK is a series of playwright automations that navigate through different sites with 

## How we built it

We spend a large amount of time determining what websites and services would have data that would be valuable to students that we could be able to pull in the timespan of a hackathon. We put together a list of services 


## Challenges we ran into

Some of the sites that we were unable to pull data from during this hackathon are listed below:

- RIT EMS Outlook API


## Accomplishments that we're proud of

The fact that the main controller can run on a arduino uno q is very cool.
Also that we did not need to use AI for the design of this 

## What we learned

## What's next for RIT SDK

We would like to add more push/write features from the SDK 

## AI Usage 

In this project, NO AI was used to generate software. Local AI models were used experimentally as a debug tool to find the cause of errors. We were able to find and resolve errors like HA calendar timeout faster than the AI could.