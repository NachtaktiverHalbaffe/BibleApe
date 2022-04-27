# BibleApe
**This is work in progress. No working prototype is availble right now**

This is intended to become a Bible Data Framework to visualize and study various data relations relying on the Bible itself. Although the Github Readme and developer docs are in english, the core/mother language is german and as a consequence some data entry keys, names etc. are named in german.

# Development documentation
## Data
The data can be gathered from different sources. For this purpose the data architecture is build up in a modular way. There a models for the data itself, there are data sources from which the Bible text itself can be gained, interfaces which defines the calls that can be made for the data and use cases which implement a interface.

### Data sources
API.bible is used as an online data source. To use it, you need to gather an API access which is limited in the free form.

### Interfaces
The interfaces define the calls you can make to gain access to the data. The implementation itself can be found at the use cases. These interfaces defines what data can be accessed from the various data sources and what parameter are needed for that call.

### Use cases
Use cases are the implementation of the interfaces. Here it can be defined how the data is gathered from the available data sources and returns the entry corresponding to the definition of the interface.