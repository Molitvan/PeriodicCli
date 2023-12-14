# Periodic Cli

Get the whole periodic table in your terminal. This was created primaryerly for blind people who can't use the standard periodic table, but can be used by anyone.

# How to install
1. Download "pse" (for Linux) or "pse.exe" (for Windows) from the [releases page](https://github.com/molitvan/PeriodicCli/releases)
2. Add it to path:
    - For Windows:
        - Move pse.exe into it's own directory
        - Search for environment variables
        - Select "Edit the system environment variables"
        - Press "Environment Variables"
        - Under system variables, find the one named "Path" and select "Edit"
        - A new window will appear. Select "New"
        - Type the directory containing the pse.exe file
        - Press ok and close everything
    - For Linux:
        - Right-click the pse file and select "Properties", then check the option to make it executable
        - Alternatively, open your terminal and type
        ```sh
        chmod +x pse
        ``````
        - Copy the pse file to your /bin folder

# Usage

First, open your terminal/cmd

To get everything about an element use:
```sh
pse \<symbol\>
```

For example, to get information about gold, use:
```sh
pse Ag
```

To get only some information, use:
```sh
pse [-h] [-z] [-a] [-m] [-g] [-p] \<symbol\>
```
The options you can use are:
- z: atomic number
- a: atomic mass
- m: average atomic mass
- g: group
- p: period

For example, to get only the atomic number of gold, use:
```sh
pse Ag -z
```

# Credits

Data (pse.csv) by [DEDOLIST](https://dedolist.com/lists/science/periodic-table-detailed/csv/)
