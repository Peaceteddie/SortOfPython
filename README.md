# SortOfPython


## Warning: Editing windows registry can cause harm to your system, do so at your own risk.

### For ease of use:
<br />In the "HKEY_CLASSES_ROOT\Directory\Background\shell\" registry path,
<br />Add a Key named what ever you feel like, with a (default) string value of "&Sort files into folders",
<br />Add a Key into the previously made Key named "command"
<br />Change the "(default)" string value to:
<br />"\<path to your pythonw.exe\>" "\<path to SortingEngine.py script\>" "%V"
<br />where you replace text in the <> with paths relevant to your computer.
