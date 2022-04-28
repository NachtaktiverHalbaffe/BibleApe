# BibleApe
**This is work in progress. No working prototype is available right now**

This is intended to become a Bible Data Framework to visualize and study various data relations relying on the Bible itself. It's my first data science project, so don't expect a perfect product from the technical perspective. The main goal is to visualize relations between topics, tags, figures and author of the different stories throughout the bible.

Although the Github Readme and developer docs are in english, the core/mother language is german and as a consequence some data entry keys, names etc. are named in german.

# Quick start guide
<!-- TODO Add quickstart -->

# Development documentation
## Data
The data can be gathered from different sources. For this purpose the data architecture is build up in a modular way. There a models for the data itself, there are data sources from which the Bible text itself can be gained, interfaces which defines the calls that can be made for the data and use cases which implement a interface.

### Data sources
API.bible is used as an online data source. To use it, you need to gather an API access which is limited in the free form.

### Interfaces
The interfaces define the calls you can make to gain access to the data. The implementation itself can be found at the use cases. These interfaces defines what data can be accessed from the various data sources and what parameter are needed for that call.

### Use cases
Use cases are the implementation of the interfaces. Here it can be defined how the data is gathered from the available data sources and returns the entry corresponding to the definition of the interface.

### Models
The data models are implemented as Python dataclasses. The data itself can be accessed via its corresponding interface. There are four elementar classes:
- **verse**: One verse. It's the only model which has actual data (the content itself) and not only metadata
- **chapter**: One Chapter. It only contains metadata and verses which holds the data itself
- **book**: One book of the bible. It only contains metadata and chapters
- **story**: A story is a logical data unit which can be a part of an chapter, a chapter, multiple chapters etc. . The difference to the other data models is that it's length isn't determined by the hierarchy of the bible (books, chapters and verses) but instead in the actual beginning and ending of the data's semantic content.

Additionally there are some constant classes provided which defines a *constant pool of tags, topics, figures* etc.. It's purpose is to standardize this data entries to simplify the analysis and to enable translation of this metadata so these of can all be the same on the dataset and only the data in the verses needs to be loaded from another dataset in case of another Bible language.

## Visualization
For simple, interactive visualizations the tool Holovid Panel will be used.

## Features
