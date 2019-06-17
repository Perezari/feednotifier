# FeedNotifier

Feed Notifier is a Windows application that resides in the system tray and 
displays pop-up notifications on your desktop when new items arrive in your 
subscribed RSS or Atom feeds.

Feed Notifier is for you if you want a news aggregator that focuses on 
real-time feed notifications and leaves out all the other stuff that comes 
with most news readers.

* Supports all common RSS and Atom web feed protocols.
* Clean look and feel, doesn’t get in your way.
* Configurable polling interval for each feed.
* Configurable popup duration.
* Configurable popup size, position and transparency.
* Configurable popup border size and color.
* Popups do not steal keyboard or mouse focus from other applications.
* Popups show item age and author.
* Navigation controls in popups to view next/previous items.
* Advanced keyword filtering options.
* Supports launching from Firefox and other browsers via feed:// protocol.
* Supports enabling/disabling individual feeds.
* Deactivates when user is idle to save bandwidth and processing time.
* Supports authenticated feeds that require a username and password.
* Supports using a proxy server.
* Displays favicon for feeds when available.
* Multi-threaded feed polling.

### Proposed changes in this fork

* [x] Port code to python 3 using 2to3
* [x] Code python 3.6 compatible
* [x] Conda environment file with dependencies
* [x] Run instructions
* [ ] Replace py2exe by nuitka, cx_freeze or pyinstaller 
* [ ] Build instructions
* [ ] Resolve all build dependencies
* [ ] Make it work with my custom feeds
* [ ] Ability to preload configuration from .ini
* [ ] Merge fixes from other forks
* [ ] Create msi package

### Python run instructions 

Have miniconda installed and added to path

```shell
git clone <repository>
cd feednotifier

conda env create -f environment.yml 
conda activate feednotifier

python main.py
```


### The URL entered does not appear to be a valid RSS/Atom feed

Fix from @developer0725

> Many users meet invalid URL message in popup window.
> Because some of feed engines don't accept custom user-agent such as "FeedNotifier/2.6 +http://www.feednotifier.com/".
> They don't send valid xml as response for feed url.
> A solution is that I change user-agent to browser's user-agent.
> I used user-agent for Chrome.
