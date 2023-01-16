# Random Fields in Anki!
## By KyloFPS

This is an addon for the popular flash card program [Anki](https://apps.ankiweb.net/), which makes it possible to have random fields on cards.

![Gif Demonstration](https://i.gyazo.com/09a084402d1619dc65829921f8eacb33.gif)


**This addon is a direct copy of these other addons, which no longer work in new versions of the program.**

- https://ankiweb.net/shared/info/1940275457
- https://ankiweb.net/shared/info/1484572887

### Purpose
I created this addon to address some of the common complaints about using Anki as a program for learning speedcubing algorithms, those being:
- Unintentional memorization of the scramble
- Wanting to practice cases from different angles
These were able to be addressed by this addon because it makes it possible to include multiple scrambles as random on the front of the card.

### Installation
Visit the addon page at https://ankiweb.net/shared/info/1639213385 and copy-paste the code into the addons menu inside of the program.

### Configuration
If you would like to use a different separator, or multiple separators, you can edit the ``__init__.py`` file to change the separator or include multiple.
You can do this by changing the line: ``separators = "|"`` to another value.

#### Example 1:
If you want to separate your random values using a comma, simply change the line to ``separators = ","``

#### Example 2:
If you want to separate your random values using either a comma or a pipe, change the line to ``separators = "|,"``.

### Extras:
Fields without any non-space characters will not be included in the random selection.
Leading/trailing spaces will be removed from the random element when it's displayed on the card.
