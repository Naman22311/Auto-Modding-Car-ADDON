# DLC Pack Installer & Manager

This project automates the extraction and installation of custom DLC packs for **Grand Theft Auto V**. It simplifies the often tedious process of managing add-on vehicle mods by efficiently handling compressed archives, identifying necessary game files, and seamlessly integrating them into your game setup.

The script performs the following key functions:
- **Automated Extraction**: Extracts `.zip` and `.rar` files containing modded car data, directly from the source folder.
- **Smart Folder Detection**: Locates folders containing the critical `dlc.rpf` file, ensuring only valid DLC packs are installed.
- **Seamless Installation**: Moves the discovered DLC packs to the appropriate `dlcpacks` directory within your GTA V installation.
- **Automated DLC Registration**: Executes the **DLCList Generator.exe**, automating the process of updating your game’s configuration to include newly added DLC packs.
- **Optional Cleanup**: Offers the choice to remove original files after successful installation, maintaining a clean working environment.

