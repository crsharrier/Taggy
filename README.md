
# Taggy
An audio file sample organizer. Taggy is a GUI app which allows you to browse all audio files in a location on your local machine, and organise them using a system of 'tags'. There will be three types of tags:
- Filename tags - automatically match patterns in the filename or parent folder. 
-  User tags - defined and assigned maually
- *(future feature)* Smart tags - automatically generated based on attributes such as genre, spectral similarity, RMS, etc.

The user can browse, edit tags, and filter by tags. The app will also have facillity to preview audio files and export the members of user tags as 'kits' (copy the files designated by a user tag, collecting them into a new directory). 

### Getting Started:
Folder of audio samples for testing. Download and unzip: 
https://drive.google.com/file/d/1SpJ0k0EsXb85hW5YFtmKQiad1lRYh6B9/view?usp=sharing

```bash
# Clone the repository
git clone https://github.com/crsharrier/Taggy.git
cd Taggy

# Create virtual environment
python3 -m venv venv 

# Activate virtual environment... 
source venv/bin/activate  # On Unix/Linux
# or
.\venv\Scripts\activate  # On Windows

#  ...and install dependencies
pip3 install -r requirements.txt

# Start program
python3 src/main.py
```
### Concepts being implemented:
**Persistence & Repository Pattern** - settings will persist between sessions using a settings.json. I want to work on two different persistence implementations for the filesystem metadata, and be able to switch between them easily using the repository pattern. This means using an AbstractRepository interface with corresponding JSONRepository and SQLRepository implementations. (Repository pattern isn't 'useful', as such, for this project - more so a learning opportunity!)

**Logger** - A custom TaggyLogger class which inherits from python's built-in Logging. Neatly collate all of those debuggy print statements into a well-organised log file, without having to comment/delete them. Also send 'status' logs to the GUI's StatusBar at the bottom of the screen.  

**Test-Driven Development** - okay, I know that proper TDD should *start* with tests... Rather, I am *starting to think about* tests! And would like to develop an appropriate suite of tests to keep the project maintainable. Perhaps next project, I'll have a good enough grasp of the architecture ahead of time to be able to write the structure tests-first.  
